# Generated by Django 5.1.1 on 2024-09-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_user_timezone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="timezone",
            field=models.CharField(
                blank=True,
                choices=[
                    ("America/Puerto_Rico", "America/Puerto_Rico"),
                    ("America/Dawson", "America/Dawson"),
                    ("America/Cuiaba", "America/Cuiaba"),
                    ("Asia/Qostanay", "Asia/Qostanay"),
                    ("Asia/Bahrain", "Asia/Bahrain"),
                    ("America/Danmarkshavn", "America/Danmarkshavn"),
                    ("Australia/Adelaide", "Australia/Adelaide"),
                    ("Etc/GMT", "Etc/GMT"),
                    ("Pacific/Apia", "Pacific/Apia"),
                    ("America/Edmonton", "America/Edmonton"),
                    ("Etc/GMT-2", "Etc/GMT-2"),
                    ("Europe/Zurich", "Europe/Zurich"),
                    ("Etc/GMT+10", "Etc/GMT+10"),
                    ("Europe/Kirov", "Europe/Kirov"),
                    ("America/Asuncion", "America/Asuncion"),
                    ("EST5EDT", "EST5EDT"),
                    ("Pacific/Fakaofo", "Pacific/Fakaofo"),
                    ("Etc/Zulu", "Etc/Zulu"),
                    ("Etc/GMT+9", "Etc/GMT+9"),
                    ("America/Porto_Velho", "America/Porto_Velho"),
                    ("America/Argentina/La_Rioja", "America/Argentina/La_Rioja"),
                    ("Australia/Eucla", "Australia/Eucla"),
                    ("Atlantic/Canary", "Atlantic/Canary"),
                    ("Australia/Sydney", "Australia/Sydney"),
                    ("America/Lower_Princes", "America/Lower_Princes"),
                    ("America/Pangnirtung", "America/Pangnirtung"),
                    ("America/Grenada", "America/Grenada"),
                    ("MST7MDT", "MST7MDT"),
                    ("Indian/Mauritius", "Indian/Mauritius"),
                    ("America/Bahia_Banderas", "America/Bahia_Banderas"),
                    ("Asia/Hovd", "Asia/Hovd"),
                    ("Pacific/Rarotonga", "Pacific/Rarotonga"),
                    ("America/Santiago", "America/Santiago"),
                    ("America/Monterrey", "America/Monterrey"),
                    ("America/St_Kitts", "America/St_Kitts"),
                    ("Pacific/Pohnpei", "Pacific/Pohnpei"),
                    ("America/Moncton", "America/Moncton"),
                    ("Pacific/Samoa", "Pacific/Samoa"),
                    ("Africa/Douala", "Africa/Douala"),
                    ("America/Chicago", "America/Chicago"),
                    ("Asia/Khandyga", "Asia/Khandyga"),
                    ("Europe/Berlin", "Europe/Berlin"),
                    ("America/Los_Angeles", "America/Los_Angeles"),
                    ("Asia/Dushanbe", "Asia/Dushanbe"),
                    ("Pacific/Efate", "Pacific/Efate"),
                    ("Africa/Casablanca", "Africa/Casablanca"),
                    ("America/Metlakatla", "America/Metlakatla"),
                    ("Europe/Bratislava", "Europe/Bratislava"),
                    ("America/Marigot", "America/Marigot"),
                    ("Australia/Melbourne", "Australia/Melbourne"),
                    ("America/Halifax", "America/Halifax"),
                    ("Etc/GMT-6", "Etc/GMT-6"),
                    ("Etc/GMT-9", "Etc/GMT-9"),
                    ("Europe/Vatican", "Europe/Vatican"),
                    ("Europe/Copenhagen", "Europe/Copenhagen"),
                    ("Pacific/Guadalcanal", "Pacific/Guadalcanal"),
                    ("Antarctica/DumontDUrville", "Antarctica/DumontDUrville"),
                    ("Asia/Jerusalem", "Asia/Jerusalem"),
                    ("Etc/GMT+2", "Etc/GMT+2"),
                    ("Pacific/Kanton", "Pacific/Kanton"),
                    ("Africa/Gaborone", "Africa/Gaborone"),
                    ("America/Punta_Arenas", "America/Punta_Arenas"),
                    ("Asia/Yangon", "Asia/Yangon"),
                    ("Etc/UCT", "Etc/UCT"),
                    ("America/Lima", "America/Lima"),
                    ("Africa/Tripoli", "Africa/Tripoli"),
                    ("PST8PDT", "PST8PDT"),
                    ("America/Nuuk", "America/Nuuk"),
                    ("America/Sitka", "America/Sitka"),
                    ("Asia/Urumqi", "Asia/Urumqi"),
                    ("Africa/Brazzaville", "Africa/Brazzaville"),
                    ("Africa/Malabo", "Africa/Malabo"),
                    ("America/Cayenne", "America/Cayenne"),
                    ("America/Indiana/Vincennes", "America/Indiana/Vincennes"),
                    ("America/Santarem", "America/Santarem"),
                    ("Asia/Jayapura", "Asia/Jayapura"),
                    ("EET", "EET"),
                    ("Australia/Currie", "Australia/Currie"),
                    ("Asia/Tokyo", "Asia/Tokyo"),
                    ("Asia/Brunei", "Asia/Brunei"),
                    ("Pacific/Noumea", "Pacific/Noumea"),
                    ("Europe/Mariehamn", "Europe/Mariehamn"),
                    ("Asia/Dhaka", "Asia/Dhaka"),
                    ("America/Detroit", "America/Detroit"),
                    ("Pacific/Niue", "Pacific/Niue"),
                    ("Europe/Minsk", "Europe/Minsk"),
                    ("Antarctica/Vostok", "Antarctica/Vostok"),
                    ("Atlantic/Madeira", "Atlantic/Madeira"),
                    ("Asia/Novosibirsk", "Asia/Novosibirsk"),
                    ("America/Fortaleza", "America/Fortaleza"),
                    ("Europe/Ulyanovsk", "Europe/Ulyanovsk"),
                    ("Asia/Bishkek", "Asia/Bishkek"),
                    ("Australia/Yancowinna", "Australia/Yancowinna"),
                    ("Asia/Hong_Kong", "Asia/Hong_Kong"),
                    ("Europe/Budapest", "Europe/Budapest"),
                    ("Indian/Mahe", "Indian/Mahe"),
                    ("America/Resolute", "America/Resolute"),
                    ("America/Dominica", "America/Dominica"),
                    ("Africa/Lagos", "Africa/Lagos"),
                    ("Europe/Monaco", "Europe/Monaco"),
                    ("Africa/Ceuta", "Africa/Ceuta"),
                    ("Etc/GMT-5", "Etc/GMT-5"),
                    ("Pacific/Marquesas", "Pacific/Marquesas"),
                    ("America/Manaus", "America/Manaus"),
                    ("Asia/Samarkand", "Asia/Samarkand"),
                    ("Africa/Mogadishu", "Africa/Mogadishu"),
                    ("America/Yellowknife", "America/Yellowknife"),
                    ("America/Santa_Isabel", "America/Santa_Isabel"),
                    ("Etc/GMT+11", "Etc/GMT+11"),
                    ("Europe/Simferopol", "Europe/Simferopol"),
                    ("America/Goose_Bay", "America/Goose_Bay"),
                    ("America/Cambridge_Bay", "America/Cambridge_Bay"),
                    ("Africa/Bujumbura", "Africa/Bujumbura"),
                    ("America/Paramaribo", "America/Paramaribo"),
                    ("Antarctica/Troll", "Antarctica/Troll"),
                    ("Europe/Paris", "Europe/Paris"),
                    ("Europe/Malta", "Europe/Malta"),
                    ("America/Aruba", "America/Aruba"),
                    ("Africa/Djibouti", "Africa/Djibouti"),
                    ("America/Glace_Bay", "America/Glace_Bay"),
                    ("Europe/Brussels", "Europe/Brussels"),
                    ("America/Vancouver", "America/Vancouver"),
                    ("Australia/Brisbane", "Australia/Brisbane"),
                    ("Africa/Mbabane", "Africa/Mbabane"),
                    ("Europe/Busingen", "Europe/Busingen"),
                    ("America/Guatemala", "America/Guatemala"),
                    ("Asia/Seoul", "Asia/Seoul"),
                    ("Pacific/Palau", "Pacific/Palau"),
                    ("Europe/Tallinn", "Europe/Tallinn"),
                    ("Etc/GMT+1", "Etc/GMT+1"),
                    ("Asia/Singapore", "Asia/Singapore"),
                    ("Pacific/Nauru", "Pacific/Nauru"),
                    ("Asia/Krasnoyarsk", "Asia/Krasnoyarsk"),
                    ("Africa/Luanda", "Africa/Luanda"),
                    ("Europe/Jersey", "Europe/Jersey"),
                    ("America/Caracas", "America/Caracas"),
                    ("Pacific/Midway", "Pacific/Midway"),
                    ("Africa/Tunis", "Africa/Tunis"),
                    ("Europe/Zagreb", "Europe/Zagreb"),
                    ("Asia/Kamchatka", "Asia/Kamchatka"),
                    ("Pacific/Pitcairn", "Pacific/Pitcairn"),
                    ("Africa/Timbuktu", "Africa/Timbuktu"),
                    ("Europe/San_Marino", "Europe/San_Marino"),
                    ("Africa/Dakar", "Africa/Dakar"),
                    ("America/Argentina/San_Luis", "America/Argentina/San_Luis"),
                    ("America/Argentina/Cordoba", "America/Argentina/Cordoba"),
                    ("Asia/Ashgabat", "Asia/Ashgabat"),
                    ("Asia/Vladivostok", "Asia/Vladivostok"),
                    ("America/Ciudad_Juarez", "America/Ciudad_Juarez"),
                    ("America/North_Dakota/New_Salem", "America/North_Dakota/New_Salem"),
                    ("America/St_Barthelemy", "America/St_Barthelemy"),
                    ("Pacific/Port_Moresby", "Pacific/Port_Moresby"),
                    ("America/Costa_Rica", "America/Costa_Rica"),
                    ("America/Phoenix", "America/Phoenix"),
                    ("Europe/Istanbul", "Europe/Istanbul"),
                    ("America/Guyana", "America/Guyana"),
                    ("America/Argentina/San_Juan", "America/Argentina/San_Juan"),
                    ("America/Iqaluit", "America/Iqaluit"),
                    ("Atlantic/Reykjavik", "Atlantic/Reykjavik"),
                    ("America/New_York", "America/New_York"),
                    ("America/La_Paz", "America/La_Paz"),
                    ("Asia/Bangkok", "Asia/Bangkok"),
                    ("Etc/GMT+12", "Etc/GMT+12"),
                    ("America/Indiana/Knox", "America/Indiana/Knox"),
                    ("America/Mazatlan", "America/Mazatlan"),
                    ("Europe/Podgorica", "Europe/Podgorica"),
                    ("America/North_Dakota/Beulah", "America/North_Dakota/Beulah"),
                    ("America/Indiana/Indianapolis", "America/Indiana/Indianapolis"),
                    ("Europe/Belgrade", "Europe/Belgrade"),
                    ("America/Whitehorse", "America/Whitehorse"),
                    ("Antarctica/Rothera", "Antarctica/Rothera"),
                    ("America/Tortola", "America/Tortola"),
                    ("Asia/Tel_Aviv", "Asia/Tel_Aviv"),
                    ("Europe/Chisinau", "Europe/Chisinau"),
                    ("Asia/Magadan", "Asia/Magadan"),
                    ("Africa/Banjul", "Africa/Banjul"),
                    ("Indian/Reunion", "Indian/Reunion"),
                    ("Europe/Bucharest", "Europe/Bucharest"),
                    ("Pacific/Funafuti", "Pacific/Funafuti"),
                    ("Europe/Vaduz", "Europe/Vaduz"),
                    ("Europe/Stockholm", "Europe/Stockholm"),
                    ("America/Indiana/Tell_City", "America/Indiana/Tell_City"),
                    ("Africa/Conakry", "Africa/Conakry"),
                    ("Europe/Amsterdam", "Europe/Amsterdam"),
                    ("Etc/GMT-14", "Etc/GMT-14"),
                    ("America/Recife", "America/Recife"),
                    ("Arctic/Longyearbyen", "Arctic/Longyearbyen"),
                    ("Africa/Kigali", "Africa/Kigali"),
                    ("America/Noronha", "America/Noronha"),
                    ("Etc/Universal", "Etc/Universal"),
                    ("America/Fort_Nelson", "America/Fort_Nelson"),
                    ("Africa/Asmara", "Africa/Asmara"),
                    ("Indian/Kerguelen", "Indian/Kerguelen"),
                    ("Pacific/Kosrae", "Pacific/Kosrae"),
                    ("Europe/Guernsey", "Europe/Guernsey"),
                    ("America/Kentucky/Louisville", "America/Kentucky/Louisville"),
                    ("Europe/Kyiv", "Europe/Kyiv"),
                    ("Asia/Almaty", "Asia/Almaty"),
                    ("Australia/Canberra", "Australia/Canberra"),
                    ("Etc/GMT-8", "Etc/GMT-8"),
                    ("WET", "WET"),
                    ("America/Argentina/Rio_Gallegos", "America/Argentina/Rio_Gallegos"),
                    ("Asia/Barnaul", "Asia/Barnaul"),
                    ("America/Tijuana", "America/Tijuana"),
                    ("Pacific/Kwajalein", "Pacific/Kwajalein"),
                    ("Europe/Tirane", "Europe/Tirane"),
                    ("America/Juneau", "America/Juneau"),
                    ("Pacific/Fiji", "Pacific/Fiji"),
                    ("America/Regina", "America/Regina"),
                    ("Etc/GMT-13", "Etc/GMT-13"),
                    ("America/Menominee", "America/Menominee"),
                    ("Asia/Harbin", "Asia/Harbin"),
                    ("Australia/Lord_Howe", "Australia/Lord_Howe"),
                    ("Indian/Maldives", "Indian/Maldives"),
                    ("America/Cayman", "America/Cayman"),
                    ("America/Inuvik", "America/Inuvik"),
                    ("Asia/Muscat", "Asia/Muscat"),
                    ("Etc/GMT+6", "Etc/GMT+6"),
                    ("Africa/Accra", "Africa/Accra"),
                    ("Etc/GMT-11", "Etc/GMT-11"),
                    ("GMT", "GMT"),
                    ("Europe/Skopje", "Europe/Skopje"),
                    ("America/Martinique", "America/Martinique"),
                    ("Pacific/Tongatapu", "Pacific/Tongatapu"),
                    ("America/Boa_Vista", "America/Boa_Vista"),
                    ("America/Rio_Branco", "America/Rio_Branco"),
                    ("Pacific/Johnston", "Pacific/Johnston"),
                    ("America/Rainy_River", "America/Rainy_River"),
                    ("Atlantic/Bermuda", "Atlantic/Bermuda"),
                    ("Asia/Omsk", "Asia/Omsk"),
                    ("Pacific/Galapagos", "Pacific/Galapagos"),
                    ("Europe/Luxembourg", "Europe/Luxembourg"),
                    ("Pacific/Majuro", "Pacific/Majuro"),
                    ("UTC", "UTC"),
                    ("Etc/UTC", "Etc/UTC"),
                    ("Etc/GMT-3", "Etc/GMT-3"),
                    ("America/Barbados", "America/Barbados"),
                    ("Asia/Kuching", "Asia/Kuching"),
                    ("America/Nome", "America/Nome"),
                    ("Asia/Ulaanbaatar", "Asia/Ulaanbaatar"),
                    ("Pacific/Wake", "Pacific/Wake"),
                    ("Australia/Perth", "Australia/Perth"),
                    ("Etc/GMT+3", "Etc/GMT+3"),
                    ("Asia/Novokuznetsk", "Asia/Novokuznetsk"),
                    ("Europe/Madrid", "Europe/Madrid"),
                    ("Pacific/Auckland", "Pacific/Auckland"),
                    ("Antarctica/Palmer", "Antarctica/Palmer"),
                    ("Asia/Yekaterinburg", "Asia/Yekaterinburg"),
                    ("Indian/Christmas", "Indian/Christmas"),
                    ("America/Argentina/Jujuy", "America/Argentina/Jujuy"),
                    ("Atlantic/Cape_Verde", "Atlantic/Cape_Verde"),
                    ("Europe/London", "Europe/London"),
                    ("MET", "MET"),
                    ("Europe/Oslo", "Europe/Oslo"),
                    ("Asia/Irkutsk", "Asia/Irkutsk"),
                    ("America/St_Lucia", "America/St_Lucia"),
                    ("Pacific/Wallis", "Pacific/Wallis"),
                    ("America/St_Johns", "America/St_Johns"),
                    ("Asia/Sakhalin", "Asia/Sakhalin"),
                    ("Europe/Isle_of_Man", "Europe/Isle_of_Man"),
                    ("Etc/GMT+8", "Etc/GMT+8"),
                    ("Asia/Tehran", "Asia/Tehran"),
                    ("Etc/GMT+4", "Etc/GMT+4"),
                    ("America/Nassau", "America/Nassau"),
                    ("Europe/Sofia", "Europe/Sofia"),
                    ("Asia/Kolkata", "Asia/Kolkata"),
                    ("Asia/Karachi", "Asia/Karachi"),
                    ("Pacific/Chuuk", "Pacific/Chuuk"),
                    ("Asia/Aqtobe", "Asia/Aqtobe"),
                    ("Asia/Taipei", "Asia/Taipei"),
                    ("HST", "HST"),
                    ("Antarctica/Mawson", "Antarctica/Mawson"),
                    ("America/Porto_Acre", "America/Porto_Acre"),
                    ("Etc/GMT+7", "Etc/GMT+7"),
                    ("America/Grand_Turk", "America/Grand_Turk"),
                    ("Europe/Astrakhan", "Europe/Astrakhan"),
                    ("Antarctica/McMurdo", "Antarctica/McMurdo"),
                    ("Indian/Comoro", "Indian/Comoro"),
                    ("Europe/Ljubljana", "Europe/Ljubljana"),
                    ("Antarctica/Casey", "Antarctica/Casey"),
                    ("Africa/Bangui", "Africa/Bangui"),
                    ("Factory", "Factory"),
                    ("Atlantic/Faroe", "Atlantic/Faroe"),
                    ("America/Shiprock", "America/Shiprock"),
                    ("Antarctica/Macquarie", "Antarctica/Macquarie"),
                    ("Atlantic/Jan_Mayen", "Atlantic/Jan_Mayen"),
                    ("Europe/Vienna", "Europe/Vienna"),
                    ("Asia/Ho_Chi_Minh", "Asia/Ho_Chi_Minh"),
                    ("Pacific/Easter", "Pacific/Easter"),
                    ("Atlantic/Stanley", "Atlantic/Stanley"),
                    ("Etc/GMT+5", "Etc/GMT+5"),
                    ("America/Sao_Paulo", "America/Sao_Paulo"),
                    ("Asia/Kuala_Lumpur", "Asia/Kuala_Lumpur"),
                    ("America/Coral_Harbour", "America/Coral_Harbour"),
                    ("Asia/Vientiane", "Asia/Vientiane"),
                    ("CST6CDT", "CST6CDT"),
                    ("Asia/Damascus", "Asia/Damascus"),
                    ("Africa/Kampala", "Africa/Kampala"),
                    ("Europe/Moscow", "Europe/Moscow"),
                    ("America/Hermosillo", "America/Hermosillo"),
                    ("Indian/Cocos", "Indian/Cocos"),
                    ("America/Indiana/Winamac", "America/Indiana/Winamac"),
                    ("Asia/Qatar", "Asia/Qatar"),
                    ("America/Yakutat", "America/Yakutat"),
                    ("Asia/Ust-Nera", "Asia/Ust-Nera"),
                    ("America/Cancun", "America/Cancun"),
                    ("Africa/Blantyre", "Africa/Blantyre"),
                    ("Asia/Kuwait", "Asia/Kuwait"),
                    ("America/Curacao", "America/Curacao"),
                    ("Pacific/Pago_Pago", "Pacific/Pago_Pago"),
                    ("Asia/Makassar", "Asia/Makassar"),
                    ("Asia/Kabul", "Asia/Kabul"),
                    ("Asia/Gaza", "Asia/Gaza"),
                    ("America/Ojinaga", "America/Ojinaga"),
                    ("America/Argentina/Mendoza", "America/Argentina/Mendoza"),
                    ("Etc/GMT-10", "Etc/GMT-10"),
                    ("Etc/GMT+0", "Etc/GMT+0"),
                    ("America/Winnipeg", "America/Winnipeg"),
                    ("America/Indiana/Marengo", "America/Indiana/Marengo"),
                    ("Africa/Lome", "Africa/Lome"),
                    ("Australia/Lindeman", "Australia/Lindeman"),
                    ("Asia/Choibalsan", "Asia/Choibalsan"),
                    ("America/Anchorage", "America/Anchorage"),
                    ("America/Jamaica", "America/Jamaica"),
                    ("America/St_Thomas", "America/St_Thomas"),
                    ("Africa/Maseru", "Africa/Maseru"),
                    ("Pacific/Guam", "Pacific/Guam"),
                    ("Pacific/Yap", "Pacific/Yap"),
                    ("Africa/Lubumbashi", "Africa/Lubumbashi"),
                    ("America/Panama", "America/Panama"),
                    ("Asia/Manila", "Asia/Manila"),
                    ("Australia/Darwin", "Australia/Darwin"),
                    ("America/Montevideo", "America/Montevideo"),
                    ("Atlantic/Azores", "Atlantic/Azores"),
                    ("Antarctica/Syowa", "Antarctica/Syowa"),
                    ("Europe/Tiraspol", "Europe/Tiraspol"),
                    ("Asia/Dubai", "Asia/Dubai"),
                    ("Africa/Niamey", "Africa/Niamey"),
                    ("America/Thunder_Bay", "America/Thunder_Bay"),
                    ("America/Ensenada", "America/Ensenada"),
                    ("America/Scoresbysund", "America/Scoresbysund"),
                    ("Asia/Qyzylorda", "Asia/Qyzylorda"),
                    ("Africa/Kinshasa", "Africa/Kinshasa"),
                    ("Asia/Tbilisi", "Asia/Tbilisi"),
                    ("Etc/GMT-12", "Etc/GMT-12"),
                    ("America/Tegucigalpa", "America/Tegucigalpa"),
                    ("Atlantic/South_Georgia", "Atlantic/South_Georgia"),
                    ("Asia/Atyrau", "Asia/Atyrau"),
                    ("America/Kralendijk", "America/Kralendijk"),
                    ("Asia/Dili", "Asia/Dili"),
                    ("America/Montserrat", "America/Montserrat"),
                    ("Africa/Ndjamena", "Africa/Ndjamena"),
                    ("Pacific/Tahiti", "Pacific/Tahiti"),
                    ("America/Havana", "America/Havana"),
                    ("America/Merida", "America/Merida"),
                    ("Pacific/Gambier", "Pacific/Gambier"),
                    ("Europe/Nicosia", "Europe/Nicosia"),
                    ("Africa/Harare", "Africa/Harare"),
                    ("Asia/Aqtau", "Asia/Aqtau"),
                    ("Africa/Dar_es_Salaam", "Africa/Dar_es_Salaam"),
                    ("Europe/Athens", "Europe/Athens"),
                    ("Etc/GMT-1", "Etc/GMT-1"),
                    ("America/Denver", "America/Denver"),
                    ("America/St_Vincent", "America/St_Vincent"),
                    ("Australia/Broken_Hill", "Australia/Broken_Hill"),
                    ("Asia/Jakarta", "Asia/Jakarta"),
                    ("Africa/Monrovia", "Africa/Monrovia"),
                    ("America/Virgin", "America/Virgin"),
                    ("Europe/Gibraltar", "Europe/Gibraltar"),
                    ("America/Argentina/Catamarca", "America/Argentina/Catamarca"),
                    ("America/Campo_Grande", "America/Campo_Grande"),
                    ("Asia/Famagusta", "Asia/Famagusta"),
                    ("America/Anguilla", "America/Anguilla"),
                    ("America/Chihuahua", "America/Chihuahua"),
                    ("Africa/Freetown", "Africa/Freetown"),
                    ("Africa/Ouagadougou", "Africa/Ouagadougou"),
                    ("Europe/Andorra", "Europe/Andorra"),
                    ("Asia/Aden", "Asia/Aden"),
                    ("Asia/Pyongyang", "Asia/Pyongyang"),
                    ("Europe/Warsaw", "Europe/Warsaw"),
                    ("Europe/Prague", "Europe/Prague"),
                    ("Asia/Shanghai", "Asia/Shanghai"),
                    ("Indian/Antananarivo", "Indian/Antananarivo"),
                    ("America/Indiana/Vevay", "America/Indiana/Vevay"),
                    ("America/Guadeloupe", "America/Guadeloupe"),
                    ("Africa/Nouakchott", "Africa/Nouakchott"),
                    ("Europe/Rome", "Europe/Rome"),
                    ("Asia/Amman", "Asia/Amman"),
                    ("Asia/Yakutsk", "Asia/Yakutsk"),
                    ("America/Port-au-Prince", "America/Port-au-Prince"),
                    ("Europe/Dublin", "Europe/Dublin"),
                    ("America/Thule", "America/Thule"),
                    ("Asia/Chongqing", "Asia/Chongqing"),
                    ("Africa/Abidjan", "Africa/Abidjan"),
                    ("Europe/Riga", "Europe/Riga"),
                    ("Pacific/Chatham", "Pacific/Chatham"),
                    ("America/El_Salvador", "America/El_Salvador"),
                    ("Africa/Windhoek", "Africa/Windhoek"),
                    ("Africa/Bissau", "Africa/Bissau"),
                    ("America/Matamoros", "America/Matamoros"),
                    ("America/Indiana/Petersburg", "America/Indiana/Petersburg"),
                    ("America/Adak", "America/Adak"),
                    ("America/Maceio", "America/Maceio"),
                    ("Asia/Riyadh", "Asia/Riyadh"),
                    ("Europe/Helsinki", "Europe/Helsinki"),
                    ("Europe/Lisbon", "Europe/Lisbon"),
                    ("America/Belem", "America/Belem"),
                    ("Europe/Belfast", "Europe/Belfast"),
                    ("America/Antigua", "America/Antigua"),
                    ("Africa/Johannesburg", "Africa/Johannesburg"),
                    ("Africa/Khartoum", "Africa/Khartoum"),
                    ("Pacific/Kiritimati", "Pacific/Kiritimati"),
                    ("Pacific/Tarawa", "Pacific/Tarawa"),
                    ("Asia/Kashgar", "Asia/Kashgar"),
                    ("America/Rankin_Inlet", "America/Rankin_Inlet"),
                    ("Etc/GMT-4", "Etc/GMT-4"),
                    ("America/Dawson_Creek", "America/Dawson_Creek"),
                    ("America/Managua", "America/Managua"),
                    ("Asia/Anadyr", "Asia/Anadyr"),
                    ("Europe/Volgograd", "Europe/Volgograd"),
                    ("America/Araguaina", "America/Araguaina"),
                    ("Asia/Srednekolymsk", "Asia/Srednekolymsk"),
                    ("America/Argentina/Salta", "America/Argentina/Salta"),
                    ("America/Miquelon", "America/Miquelon"),
                    ("Atlantic/St_Helena", "Atlantic/St_Helena"),
                    ("Africa/Libreville", "Africa/Libreville"),
                    ("Pacific/Norfolk", "Pacific/Norfolk"),
                    ("Africa/Bamako", "Africa/Bamako"),
                    ("Etc/GMT-0", "Etc/GMT-0"),
                    ("CET", "CET"),
                    ("Africa/Sao_Tome", "Africa/Sao_Tome"),
                    ("America/Atka", "America/Atka"),
                    ("America/Port_of_Spain", "America/Port_of_Spain"),
                    ("America/Santo_Domingo", "America/Santo_Domingo"),
                    ("Asia/Yerevan", "Asia/Yerevan"),
                    ("Asia/Kathmandu", "Asia/Kathmandu"),
                    ("Africa/Addis_Ababa", "Africa/Addis_Ababa"),
                    ("America/Guayaquil", "America/Guayaquil"),
                    ("Etc/GMT-7", "Etc/GMT-7"),
                    ("Asia/Macau", "Asia/Macau"),
                    ("Europe/Kaliningrad", "Europe/Kaliningrad"),
                    ("Pacific/Saipan", "Pacific/Saipan"),
                    ("Europe/Vilnius", "Europe/Vilnius"),
                    ("America/Swift_Current", "America/Swift_Current"),
                    ("America/Boise", "America/Boise"),
                    ("Africa/Maputo", "Africa/Maputo"),
                    ("Asia/Tashkent", "Asia/Tashkent"),
                    ("America/Nipigon", "America/Nipigon"),
                    ("America/Bogota", "America/Bogota"),
                    ("America/Creston", "America/Creston"),
                    ("MST", "MST"),
                    ("Etc/Greenwich", "Etc/Greenwich"),
                    ("Antarctica/Davis", "Antarctica/Davis"),
                    ("Asia/Beirut", "Asia/Beirut"),
                    ("Asia/Nicosia", "Asia/Nicosia"),
                    ("America/Kentucky/Monticello", "America/Kentucky/Monticello"),
                    ("Asia/Oral", "Asia/Oral"),
                    ("Asia/Chita", "Asia/Chita"),
                    ("Asia/Baku", "Asia/Baku"),
                    ("Indian/Mayotte", "Indian/Mayotte"),
                    ("Australia/Hobart", "Australia/Hobart"),
                    ("America/Mexico_City", "America/Mexico_City"),
                    ("Asia/Phnom_Penh", "Asia/Phnom_Penh"),
                    ("Asia/Colombo", "Asia/Colombo"),
                    ("EST", "EST"),
                    ("Asia/Baghdad", "Asia/Baghdad"),
                    ("America/Belize", "America/Belize"),
                    ("Asia/Hebron", "Asia/Hebron"),
                    ("Indian/Chagos", "Indian/Chagos"),
                    ("America/Atikokan", "America/Atikokan"),
                    ("Africa/Juba", "Africa/Juba"),
                    ("Pacific/Bougainville", "Pacific/Bougainville"),
                    ("localtime", "localtime"),
                    ("America/Montreal", "America/Montreal"),
                    ("America/Toronto", "America/Toronto"),
                    ("Africa/El_Aaiun", "Africa/El_Aaiun"),
                    ("Africa/Porto-Novo", "Africa/Porto-Novo"),
                    ("America/Eirunepe", "America/Eirunepe"),
                    ("Europe/Saratov", "Europe/Saratov"),
                    ("Africa/Cairo", "Africa/Cairo"),
                    ("Africa/Nairobi", "Africa/Nairobi"),
                    ("America/Bahia", "America/Bahia"),
                    ("Asia/Tomsk", "Asia/Tomsk"),
                    ("Europe/Samara", "Europe/Samara"),
                    ("Etc/GMT0", "Etc/GMT0"),
                    ("America/North_Dakota/Center", "America/North_Dakota/Center"),
                    ("Pacific/Honolulu", "Pacific/Honolulu"),
                    ("Europe/Sarajevo", "Europe/Sarajevo"),
                    ("America/Blanc-Sablon", "America/Blanc-Sablon"),
                    ("Asia/Istanbul", "Asia/Istanbul"),
                    ("Asia/Thimphu", "Asia/Thimphu"),
                    ("Africa/Lusaka", "Africa/Lusaka"),
                    ("America/Argentina/Ushuaia", "America/Argentina/Ushuaia"),
                    ("Africa/Algiers", "Africa/Algiers"),
                    ("America/Argentina/Buenos_Aires", "America/Argentina/Buenos_Aires"),
                    ("America/Argentina/Tucuman", "America/Argentina/Tucuman"),
                    ("Asia/Pontianak", "Asia/Pontianak"),
                ],
                max_length=128,
                null=True,
                verbose_name="timezone",
            ),
        ),
    ]
