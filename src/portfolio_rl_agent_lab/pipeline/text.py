from __future__ import annotations


def run_text_pipeline() -> None:
    from portfolio_rl_agent_lab.text.build_text_features import main as build_text_main

    build_text_main()


if __name__ == "__main__":
    run_text_pipeline()
