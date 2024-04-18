from Node import *

relationship_tree: Node = Node("Any Relationship", [
    Node("Romantic-partner", [
        Node("Wife"),
        Node("Husband")
    ]),
    Node("Family-member", [
        Node("Own-child"),
        Node("Other-relative")
    ]),
    Node("Non-family", [
        Node("Not-in-family"),
        Node("Unmarried")
    ])
])

education_tree: Node = Node("Any Education", [
    Node("Preschool"),
    Node("Elementary School",[
        Node("1st-4th"),
        Node("5th-6th"),
        Node("7th-8th")
    ]),
    Node("High School",[
        Node("9th"),
        Node("10th"),
        Node("11th"),
        Node("12th"),
        Node("HS-grad")
    ]),
    Node("College",[
        Node("Bachelors"),
        Node("Some-college"),
        Node("Prof-school"),
        Node("Assoc-acdm"),
        Node("Assoc-voc"),
        Node("Masters"),
        Node("Doctorate")
    ])
])

marital_status_tree: Node = Node("Any marital-status",[
    Node("married",[
        Node("Married-civ-spouse"),
        Node("Married-spouse-absent"),
        Node("Married-AF-spouse")
    ]),
    Node("not married",[
        Node("Never-married"),
        Node("Separated"),
        Node("Widowed"),
        Node("Divorced")
    ])
])

employment_tree: Node = Node("Any Employment",[
    Node("Private"),
    Node("Self-Employed",[
        Node("Self-emp-not-inc"),
        Node("Self-emp-inc")
    ]),
    Node("Government",[
        Node("Federal-gov"),
        Node("Local-gov"),
        Node("State-gov")
    ]),
    Node("No Pay",[
        Node("Without-pay"),
        Node("Never-worked")
    ])
])

race_tree: Node = Node("Any Race",[
    Node("White"),
    Node("Asian-Pac-Islander"),
    Node("Amer-Indian-Eskimo"),
    Node("Other"),
    Node("Black")
])

sex_tree: Node = Node("Any Sex",[
    Node("Female"),
    Node("Male")
])

native_country_tree: Node = Node("Any native country",[
    Node("Amerika",[
        Node("North America",[
            Node("United-States"),
            Node("Canada"),
            Node("Mexico")
        ]),
        Node("Central America",[
            Node("Guatemala"),
            Node("Honduras"),
            Node("Nicaragua"),
            Node("El-Salvador")
        ]),
        Node("South America",[
            Node("Peru"),
            Node("Colombia"),
            Node("Ecuador"),
            Node("Bolivia")
        ]),
        Node("Caribbean", [
            Node("Puerto-Rico"),
            Node("Cuba"),
            Node("Jamaica"),
            Node("Haiti"),
            Node("Dominican-Republic"),
            Node("Trinadad&Tobago")
        ])
    ]),
    Node("Europe",[
        Node("Western Europe",[
            Node("England"),
            Node("Germany"),
            Node("France"),
            Node("Italy"),
            Node("Spain"),
            Node("Portugal"),
            Node("Ireland"),
            Node("Scotland"),
            Node("Netherlands")
        ]),
        Node("Eastern Europe",[
            Node("Poland"),
            Node("Hungary"),
            Node("Yugoslavia")
        ]),
        Node("Northern Europe",[
            Node("Sweden"),
            Node("Norway"),
            Node("Finland"),
            Node("Denmark")
        ]),
        Node("Southern Europe",[
            Node("Greece"),
            Node("Italy"),
            Node("Portugal"),
            Node("Spain"),
            Node("France")
    ])
    ]),
    Node("Asia",[
        Node("Eastern Asia",[
            Node("Japan"),
            Node("China"),
            Node("South Korea"),
            Node("Taiwan"),
            Node("Vietnam")
        ]),
        Node("South Asia",[
            Node("India"),
            Node("Pakistan"),
            Node("Bangladesh"),
            Node("Sri Lanka")
        ]),
        Node("Southeast Asia",[
            Node("Philippines"),
            Node("Thailand"),
            Node("Cambodia"),
            Node("Laos")
        ]),
        Node("Middle East",[
            Node("Iran"),
            Node("Iraq"),
            Node("Israel"),
            Node("Saudi-Arabia"),
            Node("Turkey")
        ])
    ]),
    Node("Oceania",[
        Node("Australia"),
        Node("New-Zealand"),
        Node("Guam"),
        Node("Fiji"),
        Node("Papua-New-Guinea")
])
])

occupation_tree: Node = Node("Any occupation",[
    Node("Service",[
        Node("Tech-support"),
        Node("Craft-repair"),
        Node("Other-service"),
        Node("Priv-house-serv")
    ]),
    Node("Sales"),
    Node("Exec-managerial"),
    Node("Prof-specialty"),
    Node("Adm-clerical"),
    Node("Labor",[
        Node("Handlers-cleaners"),
        Node("Machine-op-inspct"),
        Node("Farming-fishing"),
        Node("Transport-moving")
    ]),
    Node("Protective services",[
        Node("Protective-serv"),
        Node("Armed-Forces")
    ])
])








