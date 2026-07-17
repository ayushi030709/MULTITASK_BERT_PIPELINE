from src.utils.logger import logger
from src.utils.common import set_seed

def main():

    set_seed()

    logger.info("=" * 60)
    logger.info("Starting BERT Multi-Task NLP Pipeline")
    logger.info("=" * 60)

    print("Project setup completed successfully.")
    print("Ready for Phase 2: BERT Theory + Tokenizer")

if __name__ == "__main__":
    main()