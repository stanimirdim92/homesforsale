# Generated by Django 5.1.1 on 2024-09-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_timezone_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="timezone",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Asia/Istanbul", "Asia/Istanbul"),
                    ("Africa/Windhoek", "Africa/Windhoek"),
                    ("Europe/Volgograd", "Europe/Volgograd"),
                    ("America/Belize", "America/Belize"),
                    ("Africa/Bamako", "Africa/Bamako"),
                    ("Antarctica/Casey", "Antarctica/Casey"),
                    ("Asia/Thimphu", "Asia/Thimphu"),
                    ("Europe/Skopje", "Europe/Skopje"),
                    ("America/Indiana/Winamac", "America/Indiana/Winamac"),
                    ("MST7MDT", "MST7MDT"),
                    ("Asia/Damascus", "Asia/Damascus"),
                    ("Antarctica/DumontDUrville", "Antarctica/DumontDUrville"),
                    ("America/Tortola", "America/Tortola"),
                    ("Africa/Banjul", "Africa/Banjul"),
                    ("America/Dominica", "America/Dominica"),
                    ("America/Argentina/Catamarca", "America/Argentina/Catamarca"),
                    ("Indian/Chagos", "Indian/Chagos"),
                    ("Europe/Prague", "Europe/Prague"),
                    ("Africa/Accra", "Africa/Accra"),
                    ("Europe/Isle_of_Man", "Europe/Isle_of_Man"),
                    ("Pacific/Wake", "Pacific/Wake"),
                    ("Africa/Kinshasa", "Africa/Kinshasa"),
                    ("America/Yakutat", "America/Yakutat"),
                    ("Pacific/Chatham", "Pacific/Chatham"),
                    ("Etc/GMT+7", "Etc/GMT+7"),
                    ("Europe/Busingen", "Europe/Busingen"),
                    ("Africa/Khartoum", "Africa/Khartoum"),
                    ("Atlantic/South_Georgia", "Atlantic/South_Georgia"),
                    ("Asia/Qyzylorda", "Asia/Qyzylorda"),
                    ("Africa/Algiers", "Africa/Algiers"),
                    ("Africa/Lome", "Africa/Lome"),
                    ("Europe/Warsaw", "Europe/Warsaw"),
                    ("Africa/Abidjan", "Africa/Abidjan"),
                    ("Pacific/Marquesas", "Pacific/Marquesas"),
                    ("Atlantic/St_Helena", "Atlantic/St_Helena"),
                    ("America/Argentina/Tucuman", "America/Argentina/Tucuman"),
                    ("Indian/Mahe", "Indian/Mahe"),
                    ("GMT", "GMT"),
                    ("Pacific/Johnston", "Pacific/Johnston"),
                    ("America/Bahia_Banderas", "America/Bahia_Banderas"),
                    ("America/Guyana", "America/Guyana"),
                    ("Asia/Kuala_Lumpur", "Asia/Kuala_Lumpur"),
                    ("America/El_Salvador", "America/El_Salvador"),
                    ("America/Guayaquil", "America/Guayaquil"),
                    ("America/Virgin", "America/Virgin"),
                    ("America/Yellowknife", "America/Yellowknife"),
                    ("Pacific/Wallis", "Pacific/Wallis"),
                    ("Etc/GMT-2", "Etc/GMT-2"),
                    ("Etc/GMT+0", "Etc/GMT+0"),
                    ("America/Punta_Arenas", "America/Punta_Arenas"),
                    ("America/Caracas", "America/Caracas"),
                    ("America/La_Paz", "America/La_Paz"),
                    ("America/Argentina/La_Rioja", "America/Argentina/La_Rioja"),
                    ("Africa/Dar_es_Salaam", "Africa/Dar_es_Salaam"),
                    ("America/Marigot", "America/Marigot"),
                    ("Europe/Tirane", "Europe/Tirane"),
                    ("Africa/Douala", "Africa/Douala"),
                    ("Asia/Hovd", "Asia/Hovd"),
                    ("Europe/Moscow", "Europe/Moscow"),
                    ("Etc/GMT+10", "Etc/GMT+10"),
                    ("Asia/Baghdad", "Asia/Baghdad"),
                    ("Africa/Monrovia", "Africa/Monrovia"),
                    ("Etc/GMT+3", "Etc/GMT+3"),
                    ("Asia/Pontianak", "Asia/Pontianak"),
                    ("America/Chicago", "America/Chicago"),
                    ("Asia/Jakarta", "Asia/Jakarta"),
                    ("Asia/Qatar", "Asia/Qatar"),
                    ("Asia/Amman", "Asia/Amman"),
                    ("Africa/Johannesburg", "Africa/Johannesburg"),
                    ("Etc/Greenwich", "Etc/Greenwich"),
                    ("Pacific/Tahiti", "Pacific/Tahiti"),
                    ("Etc/GMT+2", "Etc/GMT+2"),
                    ("America/Nome", "America/Nome"),
                    ("Etc/GMT+12", "Etc/GMT+12"),
                    ("Australia/Lindeman", "Australia/Lindeman"),
                    ("Europe/Riga", "Europe/Riga"),
                    ("Etc/GMT0", "Etc/GMT0"),
                    ("Europe/Monaco", "Europe/Monaco"),
                    ("Australia/Hobart", "Australia/Hobart"),
                    ("Asia/Makassar", "Asia/Makassar"),
                    ("Etc/GMT-0", "Etc/GMT-0"),
                    ("America/Noronha", "America/Noronha"),
                    ("America/Argentina/Rio_Gallegos", "America/Argentina/Rio_Gallegos"),
                    ("America/Martinique", "America/Martinique"),
                    ("Asia/Chita", "Asia/Chita"),
                    ("America/Maceio", "America/Maceio"),
                    ("Asia/Tashkent", "Asia/Tashkent"),
                    ("America/Lower_Princes", "America/Lower_Princes"),
                    ("America/Campo_Grande", "America/Campo_Grande"),
                    ("Asia/Hong_Kong", "Asia/Hong_Kong"),
                    ("America/Anguilla", "America/Anguilla"),
                    ("America/Shiprock", "America/Shiprock"),
                    ("Asia/Tel_Aviv", "Asia/Tel_Aviv"),
                    ("America/Cayman", "America/Cayman"),
                    ("Etc/GMT+11", "Etc/GMT+11"),
                    ("America/Atka", "America/Atka"),
                    ("Etc/GMT-1", "Etc/GMT-1"),
                    ("America/Cayenne", "America/Cayenne"),
                    ("Arctic/Longyearbyen", "Arctic/Longyearbyen"),
                    ("America/Phoenix", "America/Phoenix"),
                    ("America/Bahia", "America/Bahia"),
                    ("America/Nassau", "America/Nassau"),
                    ("America/Detroit", "America/Detroit"),
                    ("Europe/Zurich", "Europe/Zurich"),
                    ("Antarctica/Davis", "Antarctica/Davis"),
                    ("Asia/Brunei", "Asia/Brunei"),
                    ("Africa/Casablanca", "Africa/Casablanca"),
                    ("Asia/Anadyr", "Asia/Anadyr"),
                    ("America/Vancouver", "America/Vancouver"),
                    ("Asia/Magadan", "Asia/Magadan"),
                    ("America/Porto_Acre", "America/Porto_Acre"),
                    ("America/Montreal", "America/Montreal"),
                    ("America/North_Dakota/Beulah", "America/North_Dakota/Beulah"),
                    ("Pacific/Efate", "Pacific/Efate"),
                    ("America/Panama", "America/Panama"),
                    ("Antarctica/Troll", "Antarctica/Troll"),
                    ("Pacific/Palau", "Pacific/Palau"),
                    ("Europe/Copenhagen", "Europe/Copenhagen"),
                    ("Africa/Lagos", "Africa/Lagos"),
                    ("America/St_Vincent", "America/St_Vincent"),
                    ("America/Guadeloupe", "America/Guadeloupe"),
                    ("Asia/Baku", "Asia/Baku"),
                    ("Pacific/Tongatapu", "Pacific/Tongatapu"),
                    ("Australia/Perth", "Australia/Perth"),
                    ("America/Santarem", "America/Santarem"),
                    ("America/Rankin_Inlet", "America/Rankin_Inlet"),
                    ("Asia/Macau", "Asia/Macau"),
                    ("Europe/San_Marino", "Europe/San_Marino"),
                    ("America/Whitehorse", "America/Whitehorse"),
                    ("America/Blanc-Sablon", "America/Blanc-Sablon"),
                    ("Pacific/Guadalcanal", "Pacific/Guadalcanal"),
                    ("Europe/Jersey", "Europe/Jersey"),
                    ("Asia/Novosibirsk", "Asia/Novosibirsk"),
                    ("America/Grand_Turk", "America/Grand_Turk"),
                    ("America/Boa_Vista", "America/Boa_Vista"),
                    ("Asia/Dubai", "Asia/Dubai"),
                    ("Asia/Tokyo", "Asia/Tokyo"),
                    ("Africa/Juba", "Africa/Juba"),
                    ("Pacific/Pago_Pago", "Pacific/Pago_Pago"),
                    ("Asia/Kabul", "Asia/Kabul"),
                    ("Pacific/Nauru", "Pacific/Nauru"),
                    ("America/Cambridge_Bay", "America/Cambridge_Bay"),
                    ("America/Paramaribo", "America/Paramaribo"),
                    ("Europe/Tiraspol", "Europe/Tiraspol"),
                    ("EST", "EST"),
                    ("Etc/GMT-7", "Etc/GMT-7"),
                    ("America/Iqaluit", "America/Iqaluit"),
                    ("America/Barbados", "America/Barbados"),
                    ("Asia/Jayapura", "Asia/Jayapura"),
                    ("America/Matamoros", "America/Matamoros"),
                    ("Pacific/Chuuk", "Pacific/Chuuk"),
                    ("Antarctica/Palmer", "Antarctica/Palmer"),
                    ("America/Pangnirtung", "America/Pangnirtung"),
                    ("Antarctica/Rothera", "Antarctica/Rothera"),
                    ("Europe/Nicosia", "Europe/Nicosia"),
                    ("Europe/Madrid", "Europe/Madrid"),
                    ("Etc/GMT+5", "Etc/GMT+5"),
                    ("Africa/Maseru", "Africa/Maseru"),
                    ("Asia/Dushanbe", "Asia/Dushanbe"),
                    ("Etc/GMT-8", "Etc/GMT-8"),
                    ("Africa/Niamey", "Africa/Niamey"),
                    ("Asia/Kathmandu", "Asia/Kathmandu"),
                    ("Asia/Irkutsk", "Asia/Irkutsk"),
                    ("Asia/Shanghai", "Asia/Shanghai"),
                    ("America/Manaus", "America/Manaus"),
                    ("America/St_Lucia", "America/St_Lucia"),
                    ("America/Merida", "America/Merida"),
                    ("Pacific/Noumea", "Pacific/Noumea"),
                    ("Asia/Kolkata", "Asia/Kolkata"),
                    ("America/Cuiaba", "America/Cuiaba"),
                    ("Pacific/Apia", "Pacific/Apia"),
                    ("America/Bogota", "America/Bogota"),
                    ("America/Indiana/Vevay", "America/Indiana/Vevay"),
                    ("Asia/Tomsk", "Asia/Tomsk"),
                    ("Europe/Kaliningrad", "Europe/Kaliningrad"),
                    ("Africa/Porto-Novo", "Africa/Porto-Novo"),
                    ("Etc/GMT", "Etc/GMT"),
                    ("America/Moncton", "America/Moncton"),
                    ("Europe/Minsk", "Europe/Minsk"),
                    ("EST5EDT", "EST5EDT"),
                    ("Africa/Bangui", "Africa/Bangui"),
                    ("Africa/Ndjamena", "Africa/Ndjamena"),
                    ("Europe/Podgorica", "Europe/Podgorica"),
                    ("Europe/Athens", "Europe/Athens"),
                    ("America/Fortaleza", "America/Fortaleza"),
                    ("Etc/GMT-4", "Etc/GMT-4"),
                    ("Africa/Djibouti", "Africa/Djibouti"),
                    ("America/Dawson", "America/Dawson"),
                    ("Pacific/Auckland", "Pacific/Auckland"),
                    ("Europe/Guernsey", "Europe/Guernsey"),
                    ("Asia/Gaza", "Asia/Gaza"),
                    ("Europe/Vatican", "Europe/Vatican"),
                    ("America/Atikokan", "America/Atikokan"),
                    ("Europe/Stockholm", "Europe/Stockholm"),
                    ("America/Grenada", "America/Grenada"),
                    ("Antarctica/Syowa", "Antarctica/Syowa"),
                    ("Asia/Seoul", "Asia/Seoul"),
                    ("America/Denver", "America/Denver"),
                    ("Europe/Helsinki", "Europe/Helsinki"),
                    ("America/Havana", "America/Havana"),
                    ("Europe/Malta", "Europe/Malta"),
                    ("America/Aruba", "America/Aruba"),
                    ("Indian/Reunion", "Indian/Reunion"),
                    ("America/Argentina/Salta", "America/Argentina/Salta"),
                    ("America/Recife", "America/Recife"),
                    ("America/Los_Angeles", "America/Los_Angeles"),
                    ("Europe/Istanbul", "Europe/Istanbul"),
                    ("Africa/Libreville", "Africa/Libreville"),
                    ("Asia/Yakutsk", "Asia/Yakutsk"),
                    ("Asia/Ulaanbaatar", "Asia/Ulaanbaatar"),
                    ("Europe/Vilnius", "Europe/Vilnius"),
                    ("Pacific/Honolulu", "Pacific/Honolulu"),
                    ("Atlantic/Faroe", "Atlantic/Faroe"),
                    ("Europe/Gibraltar", "Europe/Gibraltar"),
                    ("America/Jamaica", "America/Jamaica"),
                    ("Africa/Kigali", "Africa/Kigali"),
                    ("Pacific/Norfolk", "Pacific/Norfolk"),
                    ("Africa/Nairobi", "Africa/Nairobi"),
                    ("America/Indiana/Marengo", "America/Indiana/Marengo"),
                    ("Indian/Comoro", "Indian/Comoro"),
                    ("MST", "MST"),
                    ("Etc/GMT-5", "Etc/GMT-5"),
                    ("Europe/Luxembourg", "Europe/Luxembourg"),
                    ("Atlantic/Bermuda", "Atlantic/Bermuda"),
                    ("Africa/Kampala", "Africa/Kampala"),
                    ("Africa/Blantyre", "Africa/Blantyre"),
                    ("America/Curacao", "America/Curacao"),
                    ("America/Nipigon", "America/Nipigon"),
                    ("Australia/Sydney", "Australia/Sydney"),
                    ("America/Resolute", "America/Resolute"),
                    ("Europe/Budapest", "Europe/Budapest"),
                    ("Pacific/Pitcairn", "Pacific/Pitcairn"),
                    ("Africa/Bujumbura", "Africa/Bujumbura"),
                    ("America/Menominee", "America/Menominee"),
                    ("Asia/Pyongyang", "Asia/Pyongyang"),
                    ("Africa/Nouakchott", "Africa/Nouakchott"),
                    ("Pacific/Rarotonga", "Pacific/Rarotonga"),
                    ("Asia/Sakhalin", "Asia/Sakhalin"),
                    ("Antarctica/Macquarie", "Antarctica/Macquarie"),
                    ("Asia/Kuwait", "Asia/Kuwait"),
                    ("Pacific/Majuro", "Pacific/Majuro"),
                    ("Africa/Freetown", "Africa/Freetown"),
                    ("Asia/Kashgar", "Asia/Kashgar"),
                    ("Europe/Saratov", "Europe/Saratov"),
                    ("Asia/Colombo", "Asia/Colombo"),
                    ("America/Monterrey", "America/Monterrey"),
                    ("Asia/Beirut", "Asia/Beirut"),
                    ("America/Argentina/Buenos_Aires", "America/Argentina/Buenos_Aires"),
                    ("America/Indiana/Indianapolis", "America/Indiana/Indianapolis"),
                    ("PST8PDT", "PST8PDT"),
                    ("Africa/Lusaka", "Africa/Lusaka"),
                    ("America/Glace_Bay", "America/Glace_Bay"),
                    ("CET", "CET"),
                    ("Europe/Ulyanovsk", "Europe/Ulyanovsk"),
                    ("Africa/Addis_Ababa", "Africa/Addis_Ababa"),
                    ("Etc/Zulu", "Etc/Zulu"),
                    ("Africa/Tripoli", "Africa/Tripoli"),
                    ("America/Swift_Current", "America/Swift_Current"),
                    ("Etc/GMT+8", "Etc/GMT+8"),
                    ("Etc/GMT-10", "Etc/GMT-10"),
                    ("America/Montevideo", "America/Montevideo"),
                    ("Africa/Sao_Tome", "Africa/Sao_Tome"),
                    ("America/Santo_Domingo", "America/Santo_Domingo"),
                    ("Europe/Kirov", "Europe/Kirov"),
                    ("America/Thunder_Bay", "America/Thunder_Bay"),
                    ("America/Santiago", "America/Santiago"),
                    ("Asia/Nicosia", "Asia/Nicosia"),
                    ("Asia/Novokuznetsk", "Asia/Novokuznetsk"),
                    ("America/Eirunepe", "America/Eirunepe"),
                    ("America/Anchorage", "America/Anchorage"),
                    ("Pacific/Midway", "Pacific/Midway"),
                    ("Asia/Ashgabat", "Asia/Ashgabat"),
                    ("Europe/Ljubljana", "Europe/Ljubljana"),
                    ("Australia/Canberra", "Australia/Canberra"),
                    ("America/Porto_Velho", "America/Porto_Velho"),
                    ("Atlantic/Jan_Mayen", "Atlantic/Jan_Mayen"),
                    ("America/St_Thomas", "America/St_Thomas"),
                    ("America/Managua", "America/Managua"),
                    ("America/Kralendijk", "America/Kralendijk"),
                    ("Asia/Omsk", "Asia/Omsk"),
                    ("Europe/Belfast", "Europe/Belfast"),
                    ("Asia/Aqtau", "Asia/Aqtau"),
                    ("Asia/Yangon", "Asia/Yangon"),
                    ("Pacific/Guam", "Pacific/Guam"),
                    ("Asia/Riyadh", "Asia/Riyadh"),
                    ("Indian/Kerguelen", "Indian/Kerguelen"),
                    ("Pacific/Fiji", "Pacific/Fiji"),
                    ("America/Boise", "America/Boise"),
                    ("Asia/Bishkek", "Asia/Bishkek"),
                    ("Asia/Dhaka", "Asia/Dhaka"),
                    ("America/Halifax", "America/Halifax"),
                    ("Europe/Tallinn", "Europe/Tallinn"),
                    ("Asia/Oral", "Asia/Oral"),
                    ("America/St_Johns", "America/St_Johns"),
                    ("Africa/Cairo", "Africa/Cairo"),
                    ("Africa/Ceuta", "Africa/Ceuta"),
                    ("Etc/GMT-3", "Etc/GMT-3"),
                    ("Asia/Aqtobe", "Asia/Aqtobe"),
                    ("Etc/UCT", "Etc/UCT"),
                    ("Antarctica/Vostok", "Antarctica/Vostok"),
                    ("America/Indiana/Knox", "America/Indiana/Knox"),
                    ("America/Port-au-Prince", "America/Port-au-Prince"),
                    ("Australia/Currie", "Australia/Currie"),
                    ("Pacific/Kiritimati", "Pacific/Kiritimati"),
                    ("Etc/GMT-13", "Etc/GMT-13"),
                    ("Europe/Chisinau", "Europe/Chisinau"),
                    ("Africa/Mbabane", "Africa/Mbabane"),
                    ("Etc/GMT+4", "Etc/GMT+4"),
                    ("Europe/Oslo", "Europe/Oslo"),
                    ("America/Rio_Branco", "America/Rio_Branco"),
                    ("Europe/Dublin", "Europe/Dublin"),
                    ("Asia/Bahrain", "Asia/Bahrain"),
                    ("Europe/Rome", "Europe/Rome"),
                    ("Europe/Vienna", "Europe/Vienna"),
                    ("Pacific/Tarawa", "Pacific/Tarawa"),
                    ("Africa/Mogadishu", "Africa/Mogadishu"),
                    ("Europe/Andorra", "Europe/Andorra"),
                    ("HST", "HST"),
                    ("Europe/Amsterdam", "Europe/Amsterdam"),
                    ("Africa/Timbuktu", "Africa/Timbuktu"),
                    ("America/Argentina/Mendoza", "America/Argentina/Mendoza"),
                    ("America/Ensenada", "America/Ensenada"),
                    ("America/Chihuahua", "America/Chihuahua"),
                    ("Europe/Bucharest", "Europe/Bucharest"),
                    ("Europe/Zagreb", "Europe/Zagreb"),
                    ("Asia/Vladivostok", "Asia/Vladivostok"),
                    ("Europe/Belgrade", "Europe/Belgrade"),
                    ("Asia/Aden", "Asia/Aden"),
                    ("America/Toronto", "America/Toronto"),
                    ("Pacific/Saipan", "Pacific/Saipan"),
                    ("America/Adak", "America/Adak"),
                    ("America/North_Dakota/Center", "America/North_Dakota/Center"),
                    ("Europe/Bratislava", "Europe/Bratislava"),
                    ("Africa/Luanda", "Africa/Luanda"),
                    ("Etc/GMT+1", "Etc/GMT+1"),
                    ("Europe/Mariehamn", "Europe/Mariehamn"),
                    ("Asia/Chongqing", "Asia/Chongqing"),
                    ("Pacific/Niue", "Pacific/Niue"),
                    ("Indian/Maldives", "Indian/Maldives"),
                    ("America/Mexico_City", "America/Mexico_City"),
                    ("Pacific/Galapagos", "Pacific/Galapagos"),
                    ("Pacific/Bougainville", "Pacific/Bougainville"),
                    ("Asia/Kamchatka", "Asia/Kamchatka"),
                    ("Atlantic/Stanley", "Atlantic/Stanley"),
                    ("Pacific/Gambier", "Pacific/Gambier"),
                    ("Asia/Taipei", "Asia/Taipei"),
                    ("Asia/Yerevan", "Asia/Yerevan"),
                    ("Pacific/Kwajalein", "Pacific/Kwajalein"),
                    ("Antarctica/Mawson", "Antarctica/Mawson"),
                    ("America/North_Dakota/New_Salem", "America/North_Dakota/New_Salem"),
                    ("Asia/Atyrau", "Asia/Atyrau"),
                    ("Australia/Adelaide", "Australia/Adelaide"),
                    ("Asia/Almaty", "Asia/Almaty"),
                    ("EET", "EET"),
                    ("America/Tegucigalpa", "America/Tegucigalpa"),
                    ("America/Argentina/Cordoba", "America/Argentina/Cordoba"),
                    ("Asia/Muscat", "Asia/Muscat"),
                    ("America/Puerto_Rico", "America/Puerto_Rico"),
                    ("America/Asuncion", "America/Asuncion"),
                    ("America/Hermosillo", "America/Hermosillo"),
                    ("America/St_Kitts", "America/St_Kitts"),
                    ("America/Sitka", "America/Sitka"),
                    ("Pacific/Kanton", "Pacific/Kanton"),
                    ("Etc/GMT-14", "Etc/GMT-14"),
                    ("Pacific/Kosrae", "Pacific/Kosrae"),
                    ("Asia/Tbilisi", "Asia/Tbilisi"),
                    ("America/Indiana/Tell_City", "America/Indiana/Tell_City"),
                    ("Indian/Antananarivo", "Indian/Antananarivo"),
                    ("Africa/Malabo", "Africa/Malabo"),
                    ("America/Araguaina", "America/Araguaina"),
                    ("Factory", "Factory"),
                    ("Asia/Karachi", "Asia/Karachi"),
                    ("Indian/Cocos", "Indian/Cocos"),
                    ("America/Coral_Harbour", "America/Coral_Harbour"),
                    ("Africa/Ouagadougou", "Africa/Ouagadougou"),
                    ("Europe/Lisbon", "Europe/Lisbon"),
                    ("Indian/Mauritius", "Indian/Mauritius"),
                    ("Etc/Universal", "Etc/Universal"),
                    ("Australia/Yancowinna", "Australia/Yancowinna"),
                    ("America/Goose_Bay", "America/Goose_Bay"),
                    ("Atlantic/Azores", "Atlantic/Azores"),
                    ("Pacific/Easter", "Pacific/Easter"),
                    ("Asia/Urumqi", "Asia/Urumqi"),
                    ("Antarctica/McMurdo", "Antarctica/McMurdo"),
                    ("Pacific/Fakaofo", "Pacific/Fakaofo"),
                    ("America/Regina", "America/Regina"),
                    ("Australia/Eucla", "Australia/Eucla"),
                    ("Asia/Krasnoyarsk", "Asia/Krasnoyarsk"),
                    ("America/Danmarkshavn", "America/Danmarkshavn"),
                    ("America/Metlakatla", "America/Metlakatla"),
                    ("Asia/Srednekolymsk", "Asia/Srednekolymsk"),
                    ("America/Antigua", "America/Antigua"),
                    ("Asia/Manila", "Asia/Manila"),
                    ("Africa/El_Aaiun", "Africa/El_Aaiun"),
                    ("Europe/Brussels", "Europe/Brussels"),
                    ("Pacific/Pohnpei", "Pacific/Pohnpei"),
                    ("America/Santa_Isabel", "America/Santa_Isabel"),
                    ("Africa/Brazzaville", "Africa/Brazzaville"),
                    ("Atlantic/Madeira", "Atlantic/Madeira"),
                    ("Etc/UTC", "Etc/UTC"),
                    ("America/Costa_Rica", "America/Costa_Rica"),
                    ("America/Cancun", "America/Cancun"),
                    ("Europe/Simferopol", "Europe/Simferopol"),
                    ("America/Dawson_Creek", "America/Dawson_Creek"),
                    ("Africa/Harare", "Africa/Harare"),
                    ("Asia/Dili", "Asia/Dili"),
                    ("MET", "MET"),
                    ("Asia/Qostanay", "Asia/Qostanay"),
                    ("Indian/Christmas", "Indian/Christmas"),
                    ("Asia/Barnaul", "Asia/Barnaul"),
                    ("Asia/Ust-Nera", "Asia/Ust-Nera"),
                    ("Europe/Berlin", "Europe/Berlin"),
                    ("Pacific/Port_Moresby", "Pacific/Port_Moresby"),
                    ("Africa/Dakar", "Africa/Dakar"),
                    ("Australia/Brisbane", "Australia/Brisbane"),
                    ("Europe/Kyiv", "Europe/Kyiv"),
                    ("Australia/Darwin", "Australia/Darwin"),
                    ("America/St_Barthelemy", "America/St_Barthelemy"),
                    ("Asia/Vientiane", "Asia/Vientiane"),
                    ("America/New_York", "America/New_York"),
                    ("Europe/Vaduz", "Europe/Vaduz"),
                    ("America/Creston", "America/Creston"),
                    ("America/Thule", "America/Thule"),
                    ("Asia/Hebron", "Asia/Hebron"),
                    ("Etc/GMT-11", "Etc/GMT-11"),
                    ("CST6CDT", "CST6CDT"),
                    ("Pacific/Samoa", "Pacific/Samoa"),
                    ("Europe/London", "Europe/London"),
                    ("Atlantic/Reykjavik", "Atlantic/Reykjavik"),
                    ("Asia/Harbin", "Asia/Harbin"),
                    ("Atlantic/Cape_Verde", "Atlantic/Cape_Verde"),
                    ("America/Kentucky/Louisville", "America/Kentucky/Louisville"),
                    ("Africa/Conakry", "Africa/Conakry"),
                    ("America/Inuvik", "America/Inuvik"),
                    ("Africa/Maputo", "Africa/Maputo"),
                    ("America/Argentina/San_Luis", "America/Argentina/San_Luis"),
                    ("Europe/Paris", "Europe/Paris"),
                    ("Africa/Lubumbashi", "Africa/Lubumbashi"),
                    ("UTC", "UTC"),
                    ("Africa/Gaborone", "Africa/Gaborone"),
                    ("Etc/GMT-6", "Etc/GMT-6"),
                    ("Europe/Sofia", "Europe/Sofia"),
                    ("America/Argentina/Ushuaia", "America/Argentina/Ushuaia"),
                    ("Etc/GMT+9", "Etc/GMT+9"),
                    ("America/Montserrat", "America/Montserrat"),
                    ("America/Kentucky/Monticello", "America/Kentucky/Monticello"),
                    ("Australia/Lord_Howe", "Australia/Lord_Howe"),
                    ("America/Nuuk", "America/Nuuk"),
                    ("Asia/Singapore", "Asia/Singapore"),
                    ("Europe/Sarajevo", "Europe/Sarajevo"),
                    ("America/Ojinaga", "America/Ojinaga"),
                    ("Africa/Asmara", "Africa/Asmara"),
                    ("Asia/Jerusalem", "Asia/Jerusalem"),
                    ("America/Winnipeg", "America/Winnipeg"),
                    ("Pacific/Yap", "Pacific/Yap"),
                    ("America/Fort_Nelson", "America/Fort_Nelson"),
                    ("America/Juneau", "America/Juneau"),
                    ("Asia/Kuching", "Asia/Kuching"),
                    ("Asia/Choibalsan", "Asia/Choibalsan"),
                    ("America/Mazatlan", "America/Mazatlan"),
                    ("Etc/GMT-9", "Etc/GMT-9"),
                    ("Asia/Yekaterinburg", "Asia/Yekaterinburg"),
                    ("Africa/Bissau", "Africa/Bissau"),
                    ("Australia/Broken_Hill", "Australia/Broken_Hill"),
                    ("Atlantic/Canary", "Atlantic/Canary"),
                    ("America/Rainy_River", "America/Rainy_River"),
                    ("Asia/Phnom_Penh", "Asia/Phnom_Penh"),
                    ("Asia/Ho_Chi_Minh", "Asia/Ho_Chi_Minh"),
                    ("localtime", "localtime"),
                    ("America/Ciudad_Juarez", "America/Ciudad_Juarez"),
                    ("Asia/Samarkand", "Asia/Samarkand"),
                    ("America/Indiana/Vincennes", "America/Indiana/Vincennes"),
                    ("Asia/Famagusta", "Asia/Famagusta"),
                    ("Asia/Tehran", "Asia/Tehran"),
                    ("America/Guatemala", "America/Guatemala"),
                    ("America/Port_of_Spain", "America/Port_of_Spain"),
                    ("Etc/GMT-12", "Etc/GMT-12"),
                    ("Europe/Astrakhan", "Europe/Astrakhan"),
                    ("Pacific/Funafuti", "Pacific/Funafuti"),
                    ("Europe/Samara", "Europe/Samara"),
                    ("America/Edmonton", "America/Edmonton"),
                    ("America/Scoresbysund", "America/Scoresbysund"),
                    ("America/Indiana/Petersburg", "America/Indiana/Petersburg"),
                    ("America/Sao_Paulo", "America/Sao_Paulo"),
                    ("Australia/Melbourne", "Australia/Melbourne"),
                    ("WET", "WET"),
                    ("Etc/GMT+6", "Etc/GMT+6"),
                    ("America/Tijuana", "America/Tijuana"),
                    ("America/Argentina/San_Juan", "America/Argentina/San_Juan"),
                    ("Asia/Bangkok", "Asia/Bangkok"),
                    ("Indian/Mayotte", "Indian/Mayotte"),
                    ("America/Argentina/Jujuy", "America/Argentina/Jujuy"),
                    ("America/Lima", "America/Lima"),
                    ("Asia/Khandyga", "Asia/Khandyga"),
                    ("Africa/Tunis", "Africa/Tunis"),
                    ("America/Belem", "America/Belem"),
                    ("America/Miquelon", "America/Miquelon"),
                ],
                max_length=128,
                null=True,
                verbose_name="timezone",
            ),
        ),
    ]
