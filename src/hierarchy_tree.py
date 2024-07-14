relationship_tree = {
    'name': 'Any Relationship',
    'children': [
        {
            'name': 'Romantic-partner',
            'children': [
                {'name': 'Wife'},
                {'name': 'Husband'}
            ]
        },
        {
            'name': 'Family-member',
            'children': [
                {'name': 'Own-child'},
                {'name': 'Other-relative'}
            ]
        },
        {
            'name': 'Non-family',
            'children': [
                {'name': 'Not-in-family'},
                {'name': 'Unmarried'}
            ]
        }
    ]
}

education_tree = {
    'name': 'Any Education',
    'children': [
        {'name': 'Preschool'},
        {
            'name': 'Elementary School',
            'children': [
                {'name': '1st-4th'},
                {'name': '5th-6th'},
                {'name': '7th-8th'}
            ]
        },
        {
            'name': 'High School',
            'children': [
                {'name': '9th'},
                {'name': '10th'},
                {'name': '11th'},
                {'name': '12th'},
                {'name': 'HS-grad'}
            ]
        },
        {
            'name': 'College',
            'children': [
                {'name': 'Bachelors'},
                {'name': 'Some-college'},
                {'name': 'Prof-school'},
                {'name': 'Assoc-acdm'},
                {'name': 'Assoc-voc'},
                {'name': 'Masters'},
                {'name': 'Doctorate'}
            ]
        }
    ]
}

race_tree = {
    'name': 'Any Race',
    'children': [
        {'name': 'White'},
        {'name': 'Asian-Pac-Islander'},
        {'name': 'Amer-Indian-Eskimo'},
        {'name': 'Other'},
        {'name': 'Black'}
    ]
}

marital_status_tree = {
    'name': 'Any marital-status',
    'children': [
        {
            'name': 'married',
            'children': [
                {'name': 'Married-civ-spouse'},
                {'name': 'Married-spouse-absent'},
                {'name': 'Married-AF-spouse'}
            ]
        },
        {
            'name': 'not married',
            'children': [
                {'name': 'Never-married'},
                {'name': 'Separated'},
                {'name': 'Widowed'},
                {'name': 'Divorced'}
            ]
        }
    ]
}

workclass_tree = {
    'name': 'Any Workclass',
    'children': [
        {'name': 'Private'},
        {
            'name': 'Self-Employed',
            'children': [
                {'name': 'Self-emp-not-inc'},
                {'name': 'Self-emp-inc'}
            ]
        },
        {
            'name': 'Government',
            'children': [
                {'name': 'Federal-gov'},
                {'name': 'Local-gov'},
                {'name': 'State-gov'}
            ]
        },
        {
            'name': 'No Pay',
            'children': [
                {'name': 'Without-pay'},
                {'name': 'Never-worked'}
            ]
        }
    ]
}

sex_tree = {
    'name': 'Any Sex',
    'children': [
        {'name': 'Female'},
        {'name': 'Male'}
    ]
}



native_country_tree = {
    'name': 'Any native country',
    'children': [
        {
            'name': 'Amerika',
            'children': [
                {
                    'name': 'North America',
                    'children': [
                        {'name': 'United-States'},
                        {'name': 'Canada'},
                        {'name': 'Mexico'}
                    ]
                },
                {
                    'name': 'Central America',
                    'children': [
                        {'name': 'Guatemala'},
                        {'name': 'Honduras'},
                        {'name': 'Nicaragua'},
                        {'name': 'El-Salvador'}
                    ]
                },
                {
                    'name': 'South America',
                    'children': [
                        {'name': 'Peru'},
                        {'name': 'Columbia'},
                        {'name': 'Ecuador'},
                        {'name': 'Bolivia'}
                    ]
                },
                {
                    'name': 'Caribbean',
                    'children': [
                        {'name': 'Puerto-Rico'},
                        {'name': 'Cuba'},
                        {'name': 'Jamaica'},
                        {'name': 'Haiti'},
                        {'name': 'Dominican-Republic'},
                        {'name': 'Trinadad&Tobago'}
                    ]
                },
                {
                    'name': 'Outlying-US(Guam-USVI-etc)',
                },
                {
                    'name': 'Hong'
                }
            ]
        },
        {
            'name': 'Europe',
            'children': [
                {
                    'name': 'Western Europe',
                    'children': [
                        {'name': 'England'},
                        {'name': 'Germany'},
                        {'name': 'Ireland'},
                        {'name': 'Scotland'},
                        {'name': 'Netherlands'},
                        {'name': 'Holand-Netherlands'}
                    ]
                },
                {
                    'name': 'Eastern Europe',
                    'children': [
                        {'name': 'Poland'},
                        {'name': 'Hungary'},
                        {'name': 'Yugoslavia'}
                    ]
                },
                {
                    'name': 'Northern Europe',
                    'children': [
                        {'name': 'Sweden'},
                        {'name': 'Norway'},
                        {'name': 'Finland'},
                        {'name': 'Denmark'}
                    ]
                },
                {
                    'name': 'Southern Europe',
                    'children': [
                        {'name': 'Greece'},
                        {'name': 'Italy'},
                        {'name': 'Portugal'},
                        {'name': 'Spain'},
                        {'name': 'France'}
                    ]
                }
            ]
        },
        {
            'name': 'Asia',
            'children': [
                {
                    'name': 'Eastern Asia',
                    'children': [
                        {'name': 'Japan'},
                        {'name': 'China'},
                        {'name': 'South Korea'},
                        {'name': 'Taiwan'},
                        {'name': 'Vietnam'}
                    ]
                },
                {
                    'name': 'South Asia',
                    'children': [
                        {'name': 'India'},
                        {'name': 'Pakistan'},
                        {'name': 'Bangladesh'},
                        {'name': 'Sri Lanka'}
                    ]
                },
                {
                    'name': 'Southeast Asia',
                    'children': [
                        {'name': 'Philippines'},
                        {'name': 'Thailand'},
                        {'name': 'Cambodia'},
                        {'name': 'Laos'}
                    ]
                },
                {
                    'name': 'Middle East',
                    'children': [
                        {'name': 'Iran'},
                        {'name': 'Iraq'},
                        {'name': 'Israel'},
                        {'name': 'Saudi-Arabia'},
                        {'name': 'Turkey'}
                    ]
                }
            ]
        },
        {
            'name': 'Oceania',
            'children': [
                {'name': 'Australia'},
                {'name': 'New-Zealand'},
                {'name': 'Guam'},
                {'name': 'Fiji'},
                {'name': 'Papua-New-Guinea'}
            ]
        },
{
            'name': 'South',
        },
    ]
}

occupation_tree = {
    'name': 'Any occupation',
    'children': [
        {
            'name': 'Service',
            'children': [
                {'name': 'Tech-support'},
                {'name': 'Craft-repair'},
                {'name': 'Other-service'},
                {'name': 'Priv-house-serv'}
            ]
        },
        {'name': 'Sales'},
        {'name': 'Exec-managerial'},
        {'name': 'Prof-specialty'},
        {'name': 'Adm-clerical'},
        {
            'name': 'Labor',
            'children': [
                {'name': 'Handlers-cleaners'},
                {'name': 'Machine-op-inspct'},
                {'name': 'Farming-fishing'},
                {'name': 'Transport-moving'}
            ]
        },
        {
            'name': 'Protective services',
            'children': [
                {'name': 'Protective-serv'},
                {'name': 'Armed-Forces'}
            ]
        }
    ]
}

education_tree_easy = {
    'name': 'Any Education',
    'children': [
        {
            'name': 'Secondary',
            'children' : [
                {'name': 'Primary School'},
                {'name': 'Secondary School'}
            ]
        },

        {
            'name': 'University',
            'children': [
                {'name': 'Bachelors'},
                {'name': 'Masters'},
                {'name': 'Ph.D'}
            ]
        }
    ]
}
native_country_tree_binary = {
    'name': 'Any native country',
    'children': [
        {
            'name': 'Amerika',
            'children': [
                {
                    'name': 'America A',
                    'children': [
                        {
                            'name': 'America 1',
                            'children': [
                                {
                                    'name': 'North America',
                                    'children': [
                                        {
                                            'name': 'North America -North',
                                            'children': [
                                                {'name': 'United-States'},
                                                {'name': 'Canada'}
                                            ]
                                        },
                                        {'name': 'Mexico'}
                                    ]
                                },
                                {
                                    'name': 'Central America',
                                    'children': [
                                        {
                                            'name': 'Central America -North',
                                            'children': [
                                                {'name': 'Honduras'},
                                                {'name': 'El-Salvador'}
                                            ]
                                        },
                                        {
                                            'name': 'Central America -South',
                                            'children': [
                                                {'name': 'Guatemala'},
                                                {'name': 'Nicaragua'}
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'America 2',
                            'children': [

                                {
                                    'name': 'South America',
                                    'children': [
                                        {
                                            'name': 'South America -North',
                                            'children': [
                                                {'name': 'Ecuador'},
                                                {'name': 'Columbia'}
                                            ]
                                        },
                                        {
                                            'name': 'South America -South',
                                            'children': [
                                                {'name': 'Peru'},
                                                {'name': 'Bolivia'}
                                            ]
                                        },
                                    ]
                                },
                                {
                                    'name': 'Caribbean',
                                    'children': [
                                        {
                                            'name': 'Caribbean -West',
                                            'children': [
                                                {'name': 'Jamaica'},
                                                {'name': 'Cuba'}
                                            ]
                                        },
                                        {
                                            'name': 'Caribbean -Central/East',
                                            'children': [
                                                {
                                                    'name': 'Caribbean -East',
                                                    'children': [
                                                        {'name': 'Puerto-Rico'},
                                                        {'name': 'Dominican-Republic'},
                                                    ]
                                                },
                                                {
                                                    'name': 'Caribbean -Central',
                                                    'children': [
                                                        {'name': 'Trinadad&Tobago'},
                                                        {'name': 'Haiti'}
                                                    ]
                                                }
                                            ]
                                        }

                                    ]
                                },
                            ]
                        },
                    ]
                },

                {
                    'name': 'Amerika - Other',
                    'children': [
                        {'name': 'Outlying-US(Guam-USVI-etc)'},
                        {'name': 'Hong'}
                    ]

                 }

            ]
        },
        {
            'name': 'Europe',
            'children': [
                {
                    'name': 'Europe 1',
                    'children': [
                        {
                            'name': 'Western Europe',
                            'children': [
                                {
                                    'name': 'Western Europe 1',
                                    'children': [
                                        {
                                            'name': 'Western Europe 1.1',
                                            'children': [
                                                {'name': 'England'},
                                                {'name': 'Scotland'},

                                            ]
                                        },
                                        {
                                            'name': 'Western Europe -East',
                                            'children': [
                                                {'name': 'Germany'},
                                                {'name': 'Ireland'},
                                            ]
                                        },
                                    ]
                                },
                                {
                                    'name': 'Western Europe 2',
                                    'children': [
                                        {'name': 'Netherlands'},
                                        {'name': 'Holand-Netherlands'},
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'Eastern Europe',
                            'children': [
                                {
                                    'name': 'Eastern Europe 1',
                                    'children': [
                                        {'name': 'Poland'},
                                        {'name': 'Hungary'},
                                    ]
                                },
                                {'name': 'Yugoslavia'}
                            ]
                        },
                    ]
                },
                {
                    'name': 'Europe 2',
                    'children': [
                        {
                            'name': 'Northern Europe',
                            'children': [
                                {
                                    'name': 'Northern Europe 1',
                                    'children': [
                                        {'name': 'Sweden'},
                                        {'name': 'Norway'},
                                    ]
                                },
                                {
                                    'name': 'Northern Europe 2',
                                    'children': [
                                        {'name': 'Finland'},
                                        {'name': 'Denmark'}
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'Southern Europe',
                            'children': [
                                {
                                    'name': 'Southern Europe 1',
                                    'children': [
                                        {'name': 'Greece'},
                                        {'name': 'Italy'},
                                    ]
                                },
                                {
                                    'name': 'Southern Europe 2',
                                    'children': [
                                        {'name': 'Portugal'},
                                        {'name': 'Spain'},
                                    ]
                                },
                                {'name': 'France'}

                            ]
                        }
                    ]
                }


            ]
        },
        {
            'name': 'Asia',
            'children': [
                {
                    'name': 'Asia 1',
                    'children': [
                        {
                            'name': 'Eastern Asia',
                            'children': [
                                {
                                    'name': 'Eastern Asia A',
                                    'children': [
                                        {
                                            'name': 'Eastern Asia 1',
                                            'children': [
                                                {'name': 'Japan'},
                                                {'name': 'China'}
                                            ]
                                        },
                                        {
                                            'name': 'Eastern Asia 2',
                                            'children': [
                                                {'name': 'South Korea'},
                                                {'name': 'Taiwan'}
                                            ]
                                        },
                                    ]
                                },

                                {'name': 'Vietnam'}
                            ]
                        },
                        {
                            'name': 'South Asia',
                            'children': [
                                {
                                    'name': 'South Asia 1',
                                    'children': [
                                        {'name': 'India'},
                                        {'name': 'Pakistan'}
                                    ]
                                },
                                {
                                    'name': 'South Asia 2',
                                    'children': [
                                        {'name': 'Bangladesh'},
                                        {'name': 'Sri Lanka'}
                                    ]
                                }
                            ]
                        },
                    ]
                },
                {
                    'name': 'Asia 2',
                    'children': [
                        {
                            'name': 'Southeast Asia',
                            'children': [
                                {
                                    'name': 'Southeast Asia 1',
                                    'children': [
                                        {'name': 'Philippines'},
                                        {'name': 'Thailand'}
                                    ]
                                },
                                {
                                    'name': 'Southeast Asia 2',
                                    'children': [
                                        {'name': 'Cambodia'},
                                        {'name': 'Laos'}
                                    ]
                                }
                            ]
                        },
                        {
                            'name': 'Middle East',
                            'children': [
                                {
                                    'name': 'Middle East 1',
                                    'children': [
                                        {'name': 'Iran'},
                                        {'name': 'Iraq'}
                                    ]
                                },
                                {
                                    'name': 'Middle East 2',
                                    'children': [
                                        {'name': 'Israel'},
                                        {'name': 'Saudi-Arabia'},
                                    ]
                                },
                                {'name': 'Turkey'}
                            ]
                        }
                    ]
                }


            ]
        },
        {
            'name': 'Oceania',
            'children': [
                {
                    'name': 'Oceania A',
                    'children': [
                        {
                            'name': 'Oceania 1',
                            'children': [
                                {'name': 'Australia'},
                                {'name': 'New-Zealand'}
                            ]
                        },
                        {
                            'name': 'Oceania 2',
                            'children': [
                                {'name': 'Guam'},
                                {'name': 'Fiji'}
                            ]
                        },
                    ]
                },
                {
                    'name': 'Oceania 3',
                    'children': [
                        {'name': 'Papua-New-Guinea'},
                        {'name': 'South',}
                    ]
                }
            ]
        },

    ]
}








