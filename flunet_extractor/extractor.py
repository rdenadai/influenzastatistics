import os
import time
import asyncio
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


# countries = ["Brazil"]


def run_extractor(country):
    print(f"Starting {country}")
    # To prevent download dialog
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)  # custom location
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference(
        "browser.download.dir",
        f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}",
    )
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

    # Browser
    browser = webdriver.Firefox(
        profile, executable_path=f"{os.getcwd()}/../driver/geckodriver"
    )

    N = 500
    sleep = 5e-2
    for year in range(1995, 2021):
        path = f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}/{country}-{year}.csv"
        if os.path.isfile(path):
            size = os.stat(path).st_size
            if size <= 0:
                os.remove(path)

        if not os.path.isfile(path):
            browser.get("https://apps.who.int/flumart/Default?ReportNo=12")
            # Wait page load
            k = 0
            while k <= N:
                time.sleep(sleep)
                try:
                    browser.find_element_by_id("lstSearchBy")
                    break
                except:
                    pass
                k += 1
            # Form elements
            selct = Select(browser.find_element_by_id("lstSearchBy"))
            year_from = Select(browser.find_element_by_id("ctl_list_YearFrom"))
            year_to = Select(browser.find_element_by_id("ctl_list_YearTo"))
            weak_from = Select(browser.find_element_by_id("ctl_list_WeekFrom"))
            weak_to = Select(browser.find_element_by_id("ctl_list_WeekTo"))
            btn = browser.find_element_by_id("ctl_ViewReport")
            # Set values
            selct.select_by_value(country)
            year_from.select_by_value(str(year))
            year_to.select_by_value(str(year))
            weak_from.select_by_value("1")
            weak_to.select_by_value("53")
            time.sleep(0.1)
            # Submit form
            btn.click()
            # Wait for new page
            k = 0
            while k <= N:
                time.sleep(sleep)
                try:
                    browser.find_element_by_id("ctl_ReportViewer_fixedTable")
                    break
                except:
                    pass
                k += 1
            # Download CSV!
            k = 0
            while k <= N:
                time.sleep(sleep)
                try:
                    browser.execute_script(
                        "$find('ctl_ReportViewer').exportReport('CSV');"
                    )
                    break
                except:
                    pass
                k += 1
            # Rename downloaded CSV file
            path = f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}/FluNetInteractiveReport.csv"
            k = 0
            while k <= N:
                time.sleep(sleep)
                if os.path.isfile(path):
                    os.rename(
                        path,
                        f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}/{country}-{year}.csv",
                    )
                    break
                k += 1
            print(f"Collected data for {country} / {year}")
    browser.quit()
    print(f"Collected all data for {country}")
    return 1


if __name__ == "__main__":
    os.environ["MOZ_HEADLESS"] = "1"

    if not os.path.isdir("/home/rdenadai/Projetos/covid-19-stats/data/FluNet/"):
        os.mkdir("/home/rdenadai/Projetos/covid-19-stats/data/FluNet/")
    for country in countries:
        path = f"/home/rdenadai/Projetos/covid-19-stats/data/FluNet/{country}"
        if not os.path.isdir(path):
            os.mkdir(path)

    # loop = asyncio.new_event_loop()
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        contagem = sum(list(executor.map(run_extractor, countries)))
        print(f"Total de países coletados: {contagem}")
    #    for country in countries[:5]:
    #         loop.run_in_executor(executor, run_extractor, country)
    # loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))
