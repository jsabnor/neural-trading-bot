import json
import sys

def resumir_backtest(json_path, output_path="backtest_summary.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assets = []
    for entry in data:
        m = entry["metrics"]
        asset = {
            "symbol": entry["symbol"],
            "roi": m.get("roi_net", 0) * 100,        # ROI neto en %
            "win_rate": m.get("win_rate", 0) * 100,  # Win rate en %
            "drawdown": m.get("max_drawdown", 0) * 100,  # Drawdown en %
            "sharpe": m.get("sharpe_ratio", 0),
            "trades": m.get("total_trades", 0)
        }
        assets.append(asset)

    # Top 3 por ROI
    top_roi = sorted(assets, key=lambda x: x["roi"], reverse=True)[:3]
    # Top 3 por menor Drawdown
    top_safe = sorted(assets, key=lambda x: x["drawdown"])[:3]

    resumen = {
        "summary": {
            "top_roi": [
                {"symbol": a["symbol"], "roi": a["roi"], "sharpe": a["sharpe"]}
                for a in top_roi
            ],
            "top_safe": [
                {"symbol": a["symbol"], "drawdown": a["drawdown"], "roi": a["roi"]}
                for a in top_safe
            ],
            "n_assets": len(assets)
        },
        "assets": assets
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=2, ensure_ascii=False)

    print(f"Resumen generado en {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python resume_backtest_result.py <ruta_json> [ruta_salida]")
    else:
        json_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else "backtest_summary.json"
        resumir_backtest(json_path, output_path)
