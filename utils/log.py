import logging


def configure_log():
    logging.basicConfig(level=logging.INFO,
                        filename='log_file.log',
                        filemode='a',
                        encoding = 'utf-8',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                        )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)




