"""Execute Lab 11 and persist the real model outputs in the notebook."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

here = Path(__file__).resolve().parent
notebook_path = here / "Lab11_Attention_RNN_Completed_Mohammad_Alnaghmoush.ipynb"
dataset_path = here / "dataset" / "Lab_11_QnA_Dataset.csv"

assert dataset_path.is_file(), "Original QnA dataset is required."
notebook = nbformat.read(notebook_path, as_version=4)
assert "2230004028" in notebook.cells[0].source
result = NotebookClient(
    notebook,
    timeout=1200,
    kernel_name="python3",
    resources={"metadata": {"path": str(here)}},
).execute()
nbformat.validate(result)
code_cells = [cell for cell in result.cells if cell.cell_type == "code"]
assert all(cell.execution_count is not None for cell in code_cells)
assert not [out for cell in code_cells for out in cell.get("outputs", [])
            if out.output_type == "error"]
plots = sum("image/png" in out.get("data", {})
            for cell in code_cells for out in cell.get("outputs", [])
            if out.output_type in ("display_data", "execute_result"))
assert plots >= 3, "Expected the attention visualizations"
nbformat.write(result, notebook_path)
print(f"Completed {len(code_cells)} cells; saved {plots} plots with real dataset.")
