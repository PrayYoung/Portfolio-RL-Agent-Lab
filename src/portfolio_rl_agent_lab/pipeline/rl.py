from __future__ import annotations


def run_rl_pipeline() -> None:
    from portfolio_rl_agent_lab.train.train_ppo import main as train_main
    from portfolio_rl_agent_lab.eval.backtest import main as backtest_main
    from portfolio_rl_agent_lab.eval.benchmarks import main as benchmarks_main
    from portfolio_rl_agent_lab.eval.diagnostics import main as diagnostics_main

    train_main()
    benchmarks_main()
    diagnostics_main()
    backtest_main()


if __name__ == "__main__":
    run_rl_pipeline()
