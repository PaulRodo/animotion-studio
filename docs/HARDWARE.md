# Hardware profile: NVIDIA RTX 2050 4 GB

## Observed configuration

The supplied Windows screenshots identify the adapter as `NVIDIA GeForce RTX 2050`. Task Manager showed 4.0 GB dedicated GPU memory, 7.9 GB shared GPU memory, and 15.7 GB system RAM. Shared GPU memory is borrowed system RAM; it is not equivalent to dedicated VRAM and is much slower.

## Safe starting point

- Keep batch size at 1.
- For still image generation, start at 384×384; increase to 512×512 only after a successful test.
- Prefer half precision where supported.
- Enable model offloading / low-VRAM mode if offered by the installed ComfyUI version.
- Close GPU-heavy apps and video editors first.
- Avoid multi-model workflows, ControlNet stacks, SDXL, SVD, and Wan video generation during initial tests.

## Model roles

| Tool | Intended task | Recommendation |
|---|---|---|
| Stable Diffusion 1.5 | Generate a still image / keyframe | First diffusion experiment; 4 GB is tight, not guaranteed |
| LivePortrait | Transfer face/head motion from a driving clip to a portrait | Candidate for a short trial; not general text-to-video; actual runtime VRAM must be measured |
| AnimateDiff + SD 1.5 | Generate short motion clips | Experimental only; published optimized test uses about 4.21–5.60 GB in one setup, already above/beyond the available budget |
| Wan / SVD | General video generation | Do not use as first setup on this GPU |
| AniMotion scene editor | Organize scenes, write prompts, plan shots | Use freely; does not run a heavy video diffusion model |

## Memory note

The Task Manager screenshot showed 13.4 GB of 15.7 GB system RAM in use at the time. Before model testing, close unused browser tabs/apps and check that enough system RAM is available. Don't disable the Windows pagefile to try to force more GPU memory.

## References

- ComfyUI: https://github.com/Comfy-Org/ComfyUI
- LivePortrait official repository and model files: https://github.com/KwaiVGI/LivePortrait
- AnimateDiff performance measurements: https://github.com/continue-revolution/sd-webui-animatediff/blob/master/docs/performance.md
