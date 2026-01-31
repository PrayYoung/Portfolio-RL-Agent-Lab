from __future__ import annotations


def run_student_pipeline() -> None:
    from portfolio_rl_agent_lab.student.build_student_dataset import main as build_dataset_main
    from portfolio_rl_agent_lab.student.train_student_regime import main as train_main
    from portfolio_rl_agent_lab.student.build_regime_features_student import main as infer_main

    build_dataset_main()
    train_main()
    infer_main()


if __name__ == "__main__":
    run_student_pipeline()
