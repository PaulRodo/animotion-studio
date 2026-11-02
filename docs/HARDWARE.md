# Hardware profile: NVIDIA GeForce RTX 2050 4 GB

## Known configuration

The supplied Windows screenshots identify the adapter as NVIDIA GeForce RTX 2050 with 4.0 GB dedicated GPU memory, about 7.9 GB shared GPU memory, and 15.7 GB system RAM. Shared GPU memory is borrowed system RAM; it is not equivalent to dedicated VRAM and is much slower.

## What this means for video generation

A 4 GB GPU is not a realistic target for current high-quality local text-to-video diffusion models.

- The LTX ComfyUI integration documentation currently lists a CUDA GPU with **32 GB+ VRAM** as its prerequisite.
- NVIDIA's advanced local AI video generation guide lists at least **16 GB dedicated VRAM** and recommends **64 GB system RAM**.
- The NVIDIA RTX 2050 is therefore far below the published hardware targets for those workflows. CPU offloading may prevent some immediate memory errors on some models, but can make runs extremely slow and is not a promise of compatibility.

References:
- LTX ComfyUI setup: https://docs.ltx.io/open-source-model/integration-tools/comfy-ui
- NVIDIA AI video generation guide: https://www.nvidia.com/en-us/geforce/news/rtx-ai-video-generation-guide/
- NVIDIA ComfyUI video playbook: https://build.nvidia.com/playbooks/video-gen-guide

## Reasonable local experiments

- Use batch size 1.
- For still image generation, begin at a small resolution such as 384×384; test before increasing.
- Prefer half precision where supported.
- Enable model offloading / low-VRAM mode if the installed model and ComfyUI workflow support it.
- Close GPU-heavy apps and unnecessary browser tabs.
- Avoid starting with large video models, multi-model stacks or high frame counts.
- Keep the Windows pagefile enabled; do not treat shared GPU memory as extra VRAM.

Stable Diffusion 1.5 may be a possible still-image experiment, but even that is not guaranteed to run acceptably on every 4 GB configuration. Measure actual VRAM and system RAM usage.

## What AniMotion does on this PC

- Build an editable shot plan from the creator's prompt.
- Reuse the same character description in all shot prompts.
- Submit prompts to a user-selected ComfyUI API workflow.
- Display the actual output returned by ComfyUI (video, GIF or still image).
- Edit and export image-based animations in Motion Lab.

The shot planner is deterministic prompt composition, not a hidden LLM. It adds shot size, framing, action, camera and continuity instructions. The connected model is responsible for the visual generation. Character consistency between separately generated shots is not guaranteed.

## Model roles

| Tool / model role | Intended task | Practical note |
|---|---|---|
| Lightweight text-to-image | Generate stills or keyframes | Experimental; low resolution / batch 1 |
| LivePortrait | Transfer facial motion from a driving clip to a portrait | Not general text-to-video; test VRAM before use |
| Motion Lab | Animate / edit supplied still images | Browser compositing; no AI motion synthesis |
| Modern text-to-video diffusion | Generate moving scenes from text | Not recommended on this 4 GB GPU |
