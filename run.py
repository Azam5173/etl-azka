"""
Running the ETL project
"""

import logging
import logging.config
import yaml

def main():
    """
    entry point to run the etl job
    """

    config_path = '/home/kardan/projects/project-etf/etl-azka/configs/etl_config.yml'
    config = yaml.safe_load(open(config_path))
  #  print(config)
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info('This is a TEST.')

if __name__ == '__main__':
    main()