import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def log_step(message):
    logger.info("=" * 60)
    logger.info(message)
    logger.info("=" * 60)