"""Execute Lab 12 with real Hugging Face pretrained models and save outputs."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
path = root / "Lab12_Transformers_Completed_Mohammad_Alnaghmoush.ipynb"
nb = nbformat.read(path, as_version=4)
assert "Mohammad Abdalrouf Alnaghmoush" in nb.cells[0].source
assert "2230004028" in nb.cells[0].source
nb.metadata.pop("widgets", None)
nb.metadata["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}
nbformat.validate(nb)
result = NotebookClient(
    nb,
    timeout=1800,
    kernel_name="python3",
    resources={"metadata": {"path": str(root)}},
).execute()
nbformat.validate(result)
code = [cell for cell in result.cells if cell.cell_type == "code"]
assert all(cell.execution_count is not None for cell in code)
errors = [
    out for cell in code for out in cell.get("outputs", [])
    if out.output_type == "error"
]
assert not errors, [(o.ename, o.evalue) for o in errors]
for marker in [
    "task12-architecture", "task12-extract",
    "task12-visualization", "task12-explanation-check",
]:
    cell = next(c for c in code if c.get("id") == marker)
    assert cell.outputs, "Missing task output: " + marker
output_text = "\n".join(
    "".join(out.text) if isinstance(out.text, list) else str(out.text)
    for cell in code for out in cell.outputs if out.output_type == "stream"
)
assert "Total attention heads: 144" in output_text
assert "All row sums are approximately 1: True" in output_text
plots = sum(
    "image/png" in out.get("data", {})
    for cell in code for out in cell.get("outputs", [])
    if out.output_type in ("display_data", "execute_result")
)
assert plots >= 1, "Expected a saved attention heatmap"
nbformat.write(result, path)
print(f"PASS: {len(code)} executed code cells, {plots} embedded plot(s), zero recorded errors.")
print("Task 1: 12 Transformer layers; 12 heads per layer.")
print("Task 2: 144 attention heads in total.")
print("Task 3: Real BERT third-layer, second-head attention matrix saved.")
print("Task 4: Row/column interpretation and numerical row-sum checks saved.")
