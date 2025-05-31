import csv
from pathlib import Path

def export_valgo_results_to_csv(results, output_path):
    if not results:
        print("[WARN] No hay resultados para exportar.")
        return

    keys = results[0].keys()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"[INFO] CSV exportado en: {output_path}")