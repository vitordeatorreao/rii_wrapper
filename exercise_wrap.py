"""Runs the regex wrapper on the test data"""

import io
from wrapper import RegexWrapper
from wrapper import remove_diacritics
import metrics

TEMPLATE = {
    "Brand": r"(fiat|gm|chevrolet|wv|volkswagen|ford)",
    "Model": r"(\w+)[^\w]?([a-zA-Z]\w*)?[^\w]?([a-zA-Z]\w*)?[^\w]",
    "Price": r"r\$[^\w]?(\d+\.\d+\,?\d{0,2})",
    "Motor": r"(\d\.\d)[^\w\.\,]",
    "Year": r"(\d{2,4})[^\w\.\,]",
    "Odometer": r"(\d+\.?\d+)[^\w]?kms?",
    "Fuel": r"(alcool|flex|gasolina|diesel|gvn)",
    "Gear": r"(manual|automatico)[^\w]",
    "Steering": r"(eletric\w?|hidraulic\w?|mec\w*)",
    "Color": r"(branc\w?|prata|pret\w?|cinza|vermelh\w?|marro\w?|verde|azul)",
    "Air-Conditioning": r"[^\w](ar|ac)",
    "Optionals": r"(couro|radio|cd|mp3|alarme|airbag|rodas|\d+p|\d+port\w{0,2})",
    "Complete": r"comp\w+"
}

def exercise_output(template):
    """Outputs the way specified in the exercise"""
    result = """Marca: {0}
Modelo: {1}
Preco: {2}
Motor: {3}
Ano: {4}
Km: {5}
Combustivel: {6}
Cambio: {7}
Direcao: {8}
Cor: {9}
Ar-cond: {10}
Opcionais: {11}\n"""
    return result.format(
        template["Brand"],
        template["Model"],
        template["Price"],
        template["Motor"],
        template["Year"],
        template["Odometer"],
        template["Fuel"],
        template["Gear"],
        template["Steering"],
        template["Color"],
        template["Air-Conditioning"],
        template["Optionals"]
    )

def main():
    """Main function"""
    inputs = []
    with io.open("data/test.txt", mode="r", encoding="utf-8") as file_:
        for line in file_:
            if line is not None and len(line) > 0:
                inputs += [remove_diacritics(line)]
    wrapper = RegexWrapper(TEMPLATE)
    templates = []
    for input_ in inputs:
        template = wrapper.fill_template(input_)
        print(exercise_output(template))
        templates.append(template)



    precision, recall = metrics.compute_metrics(templates)
    avg_precision = precision.mean(skipna=True)
    avg_recall = recall.mean(skipna=True)
    print('Precision:\n' +  str(precision))
    print('\nRecall:\n' +  str(recall))

    print('\n\nAverage Precision: %.4f' % avg_precision)
    print('Average Recall: %.4f' % avg_recall)


if __name__ == "__main__":
    main()
