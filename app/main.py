# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""Multi-Device Assistant — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "Multi-Device Assistant"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


threads: dict[str, list[dict]] = {}

class SyncIn(BaseModel):
    thread_id: str
    device: str
    client_message_id: str
    text: str

@app.post("/sync")
def sync(body: SyncIn):
    log = threads.setdefault(body.thread_id, [])
    if any(e.get("client_message_id") == body.client_message_id for e in log):
        return {"deduped": True, "events": log}
    seq = len(log) + 1
    log.append({"seq": seq, "device": body.device, "client_message_id": body.client_message_id, "text": body.text})
    return {"deduped": False, "events": log}

@app.get("/threads/{thread_id}")
def get_thread(thread_id: str, after_seq: int = 0):
    log = threads.get(thread_id, [])
    return {"events": [e for e in log if e["seq"] > after_seq]}
