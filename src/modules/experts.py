from pathlib import Path
from transformers import AutoModelForCausalLM

for model_name in [
    "code_alpaca",
    "cot",
    "flan_v2",
    "gemini_alpaca",
    "lima",
    "oasst1",
    "open_orca",
    "science",
    "sharegpt",
    "wizardlm",
]:
    model_path = Path(model_name)
    if model_path.exists():
        continue
    model = AutoModelForCausalLM.from_pretrained("bunsenfeng/" + model_name)
    model.save_pretrained(model_path)
