"""
Datasets registry for denguedatasets.
"""
DATASETS = {
    "dengue_bangladesh": {
        "Filename": "dengue_bangladesh.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/kawsarahmad/dengue-dataset-bangladesh",
        "License": "CC BY 4.0",
        "Description": "This dataset presents real-world data collected through surveys conducted in the Dhaka region of Bangladesh. It focuses on understanding the prevalence and characteristics of the Dengue fever phenomenon, a significant public health concern in the area. The dataset is updated monthly to reflect the evolving nature of the Dengue outbreak"
    },
    "dengue_bangladesh_mortality": {
        "Filename": "dengue_bangladesh_mortality.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/gazijahin/climatic-influence-on-dengue-mortality-2000-2024",
        "License": "MIT",
        "Description": "This dataset explores the spatio-temporal interaction between climate variability and dengue outbreaks across six divisions of Bangladesh from 2000 to 2024. It connects meteorological parameters with epidemiological indicators (cases, deaths, and case-fatality rate) to uncover how changing weather patterns influence dengue mortality"
    },
    "dengue_brazil": {
        "Filename": "dengue_brazil.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/raomuhammadsaeedali/brazil-dengue-dataset-2000-2019",
        "License": "GPL 2",
        "Description": "The dataset supplied comprises a comprehensive collection of information pertaining to numerous geographical and environmental characteristics across microregions in Brazil from 2000 to 2019. Microregion codes and names, mesoregion codes and names, state codes and names, region codes and names, biome codes and names, ecozone codes and names, climate regimes, months, years, times, dengue cases, population estimates, population density, maximum and minimum temperatures, Palmer's drought severity index, urban population percentages, access to water network percentages, and reported water shortage frequency are all included in the dataset. This information is linked to individual microregions and provides insights into population dynamics, climatic patterns, urbanization trends, water resources, and disease occurrences."
    },
    "dengue_brazil_labels": {
        "Filename": "dengue_brazil_labels.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/raomuhammadsaeedali/brazil-dengue-dataset-2000-2019",
        "License": "GPL 2",
        "Description": "Data dictionary / variable-label reference table accompanying the Brazil Dengue Dataset 2000-2019. Documents field names, codes, and descriptions used across microregion, mesoregion, state, region, biome, and ecozone identifiers, as well as climatic and demographic variables in the main dataset."
    },
    "dengue_colombia_medellin": {
        "Filename": "dengue_colombia_medellin.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/davidrestrepo/dengue",
        "License": "Unknown",
        "Description": "Dengue challenge 2- Make Health LATAM 2022. En este reto se proveerá de un dataset para cada municipio de Colombia, compuesto por los casos de dengue semana a semana entre 2007 y 2019, acompañado de otras variables sociales y climatológicas. Encontrarás además un dataset especial que hemos preparado para el municipio de Medellín, con variables climatológicas preprocesadas y una versión comprimida de imágenes satelitales para incluir en los modelos"
    },
    "dengue_colombia": {
        "Filename": "dengue_colombia.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/davidrestrepo/dengue",
        "License": "Unknown",
        "Description": "Dengue challenge 2- Make Health LATAM 2022. En este reto se proveerá de un dataset para cada municipio de Colombia, compuesto por los casos de dengue semana a semana entre 2007 y 2019, acompañado de otras variables sociales y climatológicas. Encontrarás además un dataset especial que hemos preparado para el municipio de Medellín, con variables climatológicas preprocesadas y una versión comprimida de imágenes satelitales para incluir en los modelos"
    },
    "dengue_india": {
        "Filename": "dengue_india.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/jadhavpranav/dengue-cases-in-india",
        "License": "CC0: Public Domain",
        "Description": "This data is scrapped from the National Center for Vector Borne Diseases Control. It's a website managed by the Ministry of Health & Family Welfare, Government of India. This data contains dengue cases and deaths happening in each state of India over the years."
    },
    "dengue_jakarta": {
        "Filename": "dengue_jakarta.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/yutakatarokusumah/jakarta-dengue-weather-2021-2024",
        "License": "Unknown",
        "Description": "No description available"
    },
    "dengue_pakistan": {
        "Filename": "dengue_pakistan.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/aamir28/pakistan-dengue-surveillance-data-2016-2020",
        "License": "CC BY-SA 4.0",
        "Description": "This dataset contains monthly dengue fever surveillance data from Pakistan covering the period 2016-2020. It provides comprehensive information on dengue cases and deaths across all provinces and territories, making it valuable for epidemiological research, public health policy development, and disease outbreak analysis. Time Period: January 2016 to December 2020 (5 years). Geographic Coverage: All provinces and territories of Pakistan. Frequency: Monthly aggregated data. Total Records: 420 monthly observations. Geographic Regions Included Punjab: Most populous province, Sindh: Second largest province including Karachi, KPK (Khyber Pakhtunkhwa): Northwestern province, Balochistan: Largest province by area, ICT (Islamabad Capital Territory): Federal capital territory, AJK (Azad Jammu & Kashmir): Administered territory, GB (Gilgit-Baltistan): Northern territory."
    },
    "dengue_peru": {
        "Filename": "dengue_peru.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/fazzzzzzzzzz/datos-dengue-en-el-per-2019-2022-en-csv",
        "License": "Apache 2.0",
        "Description": "No description available"
    },
    "dengue_philippines": {
        "Filename": "dengue_philippines.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/vincentgupo/dengue-cases-in-the-philippines",
        "License": "CC0: Public Domain",
        "Description": "Data set contains the recorded number of dengue cases per region of the Philippines from year 2016 to 2020. It can be used to find trends about the disease as well as spatiotemporal analysis that can result into data-driven solution about the trends of the desease for the past 5 years."
    },
    "dengue_sri_lanka": {
        "Filename": "dengue_sri_lanka.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/sadaruwan/sri-lanka-dengue-cases-2010-2020",
        "License": "Data files © Original Authors",
        "Description": "This Dataset Include Data About Sri Lanka Dengue Cases From 2010 to 2020"
    },
    "dengue_sri_lanka_2019": {
        "Filename": "dengue_sri_lanka_2019.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/kanchana1990/sri-lanka-dengue-data-2019-2021-insights",
        "License": "CC0: Public Domain",
        "Description": "A comprehensive record of dengue cases across all districts and provinces in Sri Lanka, detailing monthly occurrences from January to December for the years 2019-2021. Data serves as a critical resource for understanding the epidemiological trends of dengue, facilitating public health responses and preventive strategies. Though compact, this dataset offers rich opportunities for data science applications including trend analysis, hot spot detection, and predictive modeling for future outbreaks. Data was meticulously compiled and made available by the National Dengue Control Unit (NDCU) of Sri Lanka. For more details, visit the NDCU Dengue Information Portal."
    },
    "dengue_sri_lanka_2020": {
        "Filename": "dengue_sri_lanka_2020.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/kanchana1990/sri-lanka-dengue-data-2019-2021-insights",
        "License": "CC0: Public Domain",
        "Description": "A comprehensive record of dengue cases across all districts and provinces in Sri Lanka, detailing monthly occurrences from January to December for the years 2019-2021. Data serves as a critical resource for understanding the epidemiological trends of dengue, facilitating public health responses and preventive strategies. Though compact, this dataset offers rich opportunities for data science applications including trend analysis, hot spot detection, and predictive modeling for future outbreaks. Data was meticulously compiled and made available by the National Dengue Control Unit (NDCU) of Sri Lanka. For more details, visit the NDCU Dengue Information Portal."
    },
    "dengue_sri_lanka_2021": {
        "Filename": "dengue_sri_lanka_2021.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/kanchana1990/sri-lanka-dengue-data-2019-2021-insights",
        "License": "CC0: Public Domain",
        "Description": "A comprehensive record of dengue cases across all districts and provinces in Sri Lanka, detailing monthly occurrences from January to December for the years 2019-2021. Data serves as a critical resource for understanding the epidemiological trends of dengue, facilitating public health responses and preventive strategies. Though compact, this dataset offers rich opportunities for data science applications including trend analysis, hot spot detection, and predictive modeling for future outbreaks. Data was meticulously compiled and made available by the National Dengue Control Unit (NDCU) of Sri Lanka. For more details, visit the NDCU Dengue Information Portal."
    },
    "dengue_taiwan": {
        "Filename": "dengue_taiwan.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/taweilo/taiwan-dengue-daily-confirmed-cases-1998-2024",
        "License": "CC0: Public Domain",
        "Description": "The dataset contains detailed information on dengue fever cases since 1998, encompassing various aspects such as dates, geographical locations, and serotype details. This data can be leveraged to analyze temporal trends, spatial distribution, and the serotype of dengue cases. It is valuable for understanding the disease's progression, its impact across different regions, and the effectiveness of intervention measures over time."
    },
    "dengue_sierra_leone": {
        "Filename": "dengue_sierra_leone.csv",
        "Source": "Kaggle",
        "url": "https://www.kaggle.com/datasets/michaalmarkosesay/sierra-leone-freetown-dengueai-dataset-20152024",
        "License": "CC BY-SA 4.0",
        "Description": "Sierra Leone Freetown DengueAI Dataset (2015–2024). Offers an integrated collection of epidemiological and climatic variables specifically designed for AI-based dengue outbreak prediction and time-series modeling. The dataset captures monthly variations in temperature, humidity, and precipitation, as well as confirmed dengue cases in Freetown, Sierra Leone. Sources: OpenDengue (case surveillance) and NOAA GSOD (daily climatic records aggregated to monthly averages). Suitable for time-series forecasting, machine/deep learning models (LSTM, GRU, Transformer), epidemiological trend analysis, and AI-based health decision-support systems. Citation: Michael Marko Sesay (2025), Sierra Leone Freetown DengueAI Dataset (2015-2024), Kaggle, https://doi.org/10.34740/KAGGLE/DSV/13257213"
    },
}

__all__ = ["DATASETS"]
