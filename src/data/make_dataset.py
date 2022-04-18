import logging
import os

import click
from interim import interim

import src.config as config


@click.command()
@click.option("--input_dir", type=click.Path(exists=True))
@click.option("--subset", type=click.STRING)
@click.option("--output_dir", type=click.Path())
def main(input_dir: str, subset: str, output_dir: str) -> None:
    """
    Run data processing scripts to turn raw (../raw) data into processed data to be saved in ../processed

    :param input_dir: File path of raw data
    :param subset: Process train or test data
    :param output_dir: File path in which to save processed data
    :return:
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Making {subset} dataset from raw data")

    if not subset:
        subset = "train"

    if not input_dir:
        input_dir = config.RAW_DIR

    if not output_dir:
        output_dir = config.PROCESSED_DIR

    df = interim(subset, input_dir)

    return df


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
