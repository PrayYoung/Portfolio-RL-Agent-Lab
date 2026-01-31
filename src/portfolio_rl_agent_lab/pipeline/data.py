from __future__ import annotations


def run_data_pipeline() -> None:
    from portfolio_rl_agent_lab.data.download import main as download_main
    from portfolio_rl_agent_lab.data.make_dataset import main as make_dataset_main

    download_main()
    make_dataset_main()


if __name__ == "__main__":
    run_data_pipeline()
