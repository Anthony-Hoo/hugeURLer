import pageGen
import csvUtil

def importConfig():
    data = csvUtil.readCSVByline()
    for config in data:
        pageGen.pageGen(config[0], config[1])

if __name__ == "__main__":
    importConfig()