# Design: Multi-Device Assistant

**Project:** `multi-device-assistant`  
**Parent system design:** `10-global-realtime-product-surface.md / 02`

## 1. What this POC demonstrates

Thread event log with seq + client_message_id dedupe for phone/laptop sync.

## 2. Architecture (POC)

```text
POST /sync → append or dedupe
GET /threads/{id}?after_seq=
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Append-only seq log | Devices converge by reading forward. | `seq` numbers. |
| Idempotent device sends | Offline queues retry. | `client_message_id` dedupe. |
| after_seq pull | Efficient sync without full rewind. | Query param filter. |

## 4. Key endpoints

`GET /health`, `POST /sync`, `GET /threads/{thread_id}`

## 5. Tradeoffs / POC limits

No push/notifier channel.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Multi Device Assistant — System Design #Shorts](https://youtu.be/sfhyRIwcE34)
>
> Direct link: **https://youtu.be/sfhyRIwcE34**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

