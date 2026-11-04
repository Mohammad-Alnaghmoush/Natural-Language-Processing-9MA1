"""Run the original Lab 7 transformer model examples and save real notebook outputs."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

path = Path(__file__).resolve().parent / "Lab7_LLMs_Completed.ipynb"
nb = nbformat.read(path, as_version=4)
if not any("2230004028" in str(cell.source) for cell in nb.cells):
    intro = nbformat.v4.new_code_cell("# Student Name: Mohammad Abdalrouf Alnaghmoush\n# Student ID: 2230004028")
    nb.cells.insert(0, intro)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata.pop("widgets", None)
result = NotebookClient(
    nb, timeout=1200, kernel_name="python3",
    resources={"metadata": {"path": str(path.parent)}},
).execute()
nbformat.validate(result)
code_cells = [cell for cell in result.cells if cell.cell_type == "code"]
errors = [out for cell in code_cells for out in cell.get("outputs", []) if out.output_type == "error"]
assert not errors, [(out.ename, out.evalue) for out in errors]
assert all(cell.execution_count is not None for cell in code_cells), "Unexecuted cells remain"
task_markers = ["Task 1 — Model Families", "Task 2 — Encoder-only Model",
                "Task 3 — Encoder–Decoder Model", "Optional Challenge"]
for marker in task_markers:
    matching = [cell for cell in code_cells if marker in cell.source]
    assert matching and matching[0].outputs, "Missing real output for " + marker
nbformat.write(result, path)
print("Lab 7 executed successfully:", len(code_cells), "code cells")
for cell in code_cells:
    if "Task " in cell.source or "Optional Challenge" in cell.source:
        print(cell.source.splitlines()[0], "=>", len(cell.outputs), "outputs")
