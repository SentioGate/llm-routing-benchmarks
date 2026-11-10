#!/usr/bin/env python3
"""
Synthetic LLM gateway benchmark demonstration.

Makes no network requests and measures nothing: the numbers below are generated
deterministically to show the report format. They are not SentioGate, provider or
competitor measurements. See https://sentiogate.app/benchmarks for live metrics.
"""
import argparse
import statistics

try:
    from tabulate import tabulate
except ImportError:
    # Standard-library fallback table formatter if tabulate is not installed
    def tabulate(rows, headers, tablefmt="github"):
        all_rows = [headers] + rows
        col_widths = [max(len(str(r[i])) for r in all_rows) for i in range(len(headers))]
        sep = "| " + " | ".join("-" * w for w in col_widths) + " |"
        out = []
        out.append("| " + " | ".join(str(headers[i]).ljust(col_widths[i]) for i in range(len(headers))) + " |")
        out.append(sep)
        for row in rows:
            out.append("| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))) + " |")
        return "\n".join(out)


def simulate_benchmark(iterations: int = 20):
    print(f"\n🚀 Generating {iterations} synthetic samples (no network, not real measurements)...")

    # Deterministic placeholder samples that only illustrate the table layout.
    direct_baseline = [180 + (i % 7) * 4 for i in range(iterations)]
    via_gateway = [196 + (i % 5) * 3 for i in range(iterations)]

    results = [
        ["Direct provider call (synthetic)", f"{statistics.mean(direct_baseline):.1f} ms", f"{statistics.median(direct_baseline):.1f} ms", "0 ms"],
        ["Via gateway (synthetic)", f"{statistics.mean(via_gateway):.1f} ms", f"{statistics.median(via_gateway):.1f} ms", f"+{statistics.mean(via_gateway) - statistics.mean(direct_baseline):.1f} ms"],
    ]

    print("\n" + tabulate(results, headers=["Sample set", "Mean", "Median", "Difference"], tablefmt="github"))
    print("\n⚠️  Synthetic demo values only. Live metrics: https://sentiogate.app/benchmarks\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a synthetic LLM gateway benchmark demonstration")
    parser.add_argument("--iterations", type=int, default=20, help="Number of synthetic samples (1-10000)")
    args = parser.parse_args()
    if not 1 <= args.iterations <= 10000:
        parser.error("--iterations must be between 1 and 10000")
    simulate_benchmark(args.iterations)
