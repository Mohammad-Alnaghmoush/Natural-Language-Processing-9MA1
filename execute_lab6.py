"""Execute both existing Lab 6 notebooks using the original labeled Yelp dataset."""
from pathlib import Path
import pandas as pd
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
dataset = root / "07-yelp-dataset.txt"
assert dataset.is_file(), "The original Yelp sentiment data is missing."
frame = pd.read_csv(dataset, sep="\t", names=["review", "label"])
assert len(frame) == 1000
assert frame["label"].value_counts().to_dict() == {0: 500, 1: 500}
print("Verified Yelp data:", len(frame), "genuine reviews.")

paths = [root / "lab6_NLP.ipynb", root / "lab6__NLP.ipynb"]
for path in paths:
    nb = nbformat.read(path, as_version=4)
    assert "2230004028" in nb.cells[0].source
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    result = NotebookClient(nb, timeout=1000, kernel_name="python3",
                            resources={"metadata": {"path": str(root)}}).execute()
    nbformat.validate(result)
    codes = [c for c in result.cells if c.cell_type == "code"]
    assert all(c.execution_count is not None for c in codes)
    errors = [o for c in codes for o in c.get("outputs", []) if o.output_type == "error"]
    assert not errors, [(o.ename, o.evalue) for o in errors]
    output_text = "\n".join(
        "".join(o.text) if isinstance(o.text, list) else str(o.text)
        for c in codes for o in c.get("outputs", []) if o.output_type == "stream"
    )
    assert "Test Accuracy" in output_text and "Classification Report" in output_text
    if path.name == "lab6__NLP.ipynb":
        assert "Training tensor shape" in output_text
    nbformat.write(result, path)
    print("Saved real run:", path.name, len(codes), "executed cells")
    print(output_text[-600:])
