import pageGen
import csvUtil


def import_config():
    data = csvUtil.read_csv_byline()
    for config in data:
        pageGen.page_gen(config[0], config[1])


if __name__ == "__main__":
    import_config()
