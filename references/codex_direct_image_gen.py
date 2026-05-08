"""Direct Codex Responses gpt-image-2 high-quality portrait at custom size."""
import sys, os, base64, time

hermes_home = os.environ.get(
    "HERMES_AGENT_HOME",
    os.path.expanduser("~/.hermes/hermes-agent"),
)
plugin_dir = os.path.join(hermes_home, "plugins/image_gen/openai-codex")
sys.path.insert(0, hermes_home)
sys.path.insert(0, plugin_dir)

import importlib.util
spec = importlib.util.spec_from_file_location(
    "codex_img_plugin",
    os.path.join(plugin_dir, "__init__.py")
)
plugin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plugin)

client = plugin._build_codex_client()
if client is None:
    print("ERROR: could not build Codex client", file=sys.stderr)
    sys.exit(2)

prompt_path = sys.argv[1]
out_path = sys.argv[2]
size = sys.argv[3] if len(sys.argv) > 3 else "2048x3072"
quality = sys.argv[4] if len(sys.argv) > 4 else "high"

with open(prompt_path) as f:
    prompt = f.read()

print(f"Prompt chars: {len(prompt)}")
print(f"Size: {size}, Quality: {quality}")
t0 = time.time()

image_b64 = None
with client.responses.stream(
    model="gpt-5.4",
    store=False,
    instructions="You are an assistant that must fulfill image generation requests by using the image_generation tool when provided.",
    input=[{
        "type": "message",
        "role": "user",
        "content": [{"type": "input_text", "text": prompt}],
    }],
    tools=[{
        "type": "image_generation",
        "model": "gpt-image-2",
        "size": size,
        "quality": quality,
        "output_format": "png",
        "background": "opaque",
        "partial_images": 1,
    }],
    tool_choice={
        "type": "allowed_tools",
        "mode": "required",
        "tools": [{"type": "image_generation"}],
    },
) as stream:
    for event in stream:
        et = getattr(event, "type", "")
        if et == "response.output_item.done":
            item = getattr(event, "item", None)
            if getattr(item, "type", None) == "image_generation_call":
                result = getattr(item, "result", None)
                if isinstance(result, str) and result:
                    image_b64 = result
        elif et == "response.error":
            print("ERROR event:", event, file=sys.stderr)

if not image_b64:
    print("ERROR: no image returned", file=sys.stderr)
    sys.exit(3)

with open(out_path, "wb") as f:
    f.write(base64.b64decode(image_b64))

dt = time.time() - t0
print(f"Saved {out_path} (elapsed {dt:.1f}s)")
