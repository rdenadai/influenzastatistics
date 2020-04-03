import os
import sys
import pandas as pd


countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Angola",
    "Anguilla",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Bermuda",
    "Bhutan",
    "Bolivia (Plurinational State of)",
    "Bosnia and Herzegovina",
    "Brazil",
    "Bulgaria",
    "Burkina Faso",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Congo",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czechia",
    "Democratic People's Republic of Korea",
    "Democratic Republic of the Congo",
    "Denmark",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "French Guiana",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Guadeloupe",
    "Guatemala",
    "Guinea",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran (Islamic Republic of)",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kosovo (in accordance with Security Council resolution 1244 (1999))",
    "Kuwait",
    "Kyrgyzstan",
    "Lao People's Democratic Republic",
    "Latvia",
    "Lebanon",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Mongolia",
    "Montenegro",
    "Montserrat",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Nepal",
    "Netherlands",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Republic of Korea",
    "Republic of Moldova",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Barthelemy",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Martin",
    "Saint Vincent and the Grenadines",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syrian Arab Republic",
    "Tajikistan",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks and Caicos Is.",
    "Uganda",
    "Ukraine",
    "United Kingdom of Great Britain and Northern Ireland",
    "United Republic of Tanzania",
    "United States of America",
    "Uruguay",
    "Uzbekistan",
    "Venezuela (Bolivarian Republic of)",
    "Viet Nam",
    "West Bank and Gaza Strip",
    "Yemen",
    "Zambia",
]


if __name__ == "__main__":

    lidf = []
    for country in countries:
        try:
            os.remove(
                f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}/FluNetInteractiveReport.csv"
            )
        except:
            pass

        lidfp = []
        for year in range(1995, 2022):
            path = f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}/{country}-{year}.csv"
            if os.path.isfile(path):
                size = os.stat(path).st_size
                if size <= 0:
                    os.remove(path)
                else:
                    content = None
                    with open(path, "r") as fr:
                        content = fr.readlines()
                    if "textbox22" in content[0]:
                        with open(path, "w") as fw:
                            fw.write("\n".join(content[3:]))

                    try:
                        df = pd.read_csv(path)
                        lidf.append(df.copy())
                        lidfp.append(df.copy())
                    except:
                        print(f"ERROR: {country}/{country}-{year}.csv")

        if len(lidfp) > 0:
            dfp = pd.concat(lidfp, axis=0, ignore_index=True)
            dfp.to_csv(
                f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}_dataset.csv"
            )

    if len(lidf) > 0:
        df = pd.concat(lidf, axis=0, ignore_index=True)
        df.to_csv("/home/rdenadai/Projetos/covid-19-stats/data/FluNet/full_dataset.csv")
