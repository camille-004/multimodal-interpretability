import logging

import click


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath: str, output_filepath: str) -> None:
    """
    Run data processing scripts to turn raw (../raw) data into processed data to be saved in ../processed

    :param input_filepath: File path of raw data
    :param output_filepath: File path in which to save processed data
    :return:
    """
    logger = logging.getLogger(__name__)
    logger.info("Making final dataset from raw data")

    # Call data processing functions here


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
