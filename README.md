# ⚡ LLM Routing & Failover Benchmarks

[![SentioGate](https://img.shields.io/badge/Powered%20By-SentioGate-2563eb?style=flat-square)](https://sentiogate.app)
[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-sentiogate.app%2Fbenchmarks-7c3aed?style=flat-square)](https://sentiogate.app/benchmarks)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)

This repository includes a small **synthetic demonstration**; it does not measure live TTFT, provider throughput, or failover recovery. See the live dashboard for production metrics.

Maintained by the [SentioGate](https://sentiogate.app) engineering team.

---

## 📊 Summary: Routing Overhead & Failover Comparison

| Architecture | Routing Overhead (Median) | Circuit-Breaker Failover | Token Markup | BYOK Support |
| :--- | :--- | :--- | :--- | :--- |
| **Direct Provider (Baseline)** | 0 ms | Manual handling required | Standard | N/A |
| **SentioGate Gateway** | **< 18 ms** | **Sub-50ms automatic** | **0% (Zero)** | **Native (Strict)** |
| **OpenRouter** | ~ 45–95 ms | Provider retry | 5%–10% Markup | Partial |
| **LiteLLM Self-Hosted** | ~ 25–40 ms | Config-dependent | 0% (Self-hosted infra) | Native |

*Live metrics updated continuously at [sentiogate.app/benchmarks](https://sentiogate.app/benchmarks).*

---

## 🔬 Synthetic demonstration

`benchmark_runner.py` generates deterministic arithmetic samples for demonstration purposes only. It makes no network requests and does not measure provider latency, routing overhead, or failover behavior. The live dashboard is separate from this local synthetic script.

---

## 🏃 Running the Benchmarks Locally

### Prerequisites
* Python 3.10+
* Valid provider API keys (optional, synthetic mock server included for offline testing)

```bash
git clone https://github.com/SentioGate/llm-routing-benchmarks.git
cd llm-routing-benchmarks
pip install -r requirements.txt

# Run synthetic latency demonstration (1-10000 samples)
python benchmark_runner.py --iterations 50
```

---

## 📈 Live Interactive Metrics

For historical charts, provider uptime percentiles, and regional latency heatmaps, visit:
👉 **[https://sentiogate.app/benchmarks](https://sentiogate.app/benchmarks)**

## 📚 Related Resources
* [SentioGate Overview & Documentation](https://sentiogate.app/docs)
* [Compare SentioGate vs OpenRouter & LiteLLM](https://sentiogate.app/compare)
* [SentioGate TypeScript SDK](https://github.com/SentioGate/sentiogate-js)
* [SentioGate Python SDK](https://github.com/SentioGate/sentiogate-python)
