# Generated by Django 5.1.1 on 2024-09-18 12:02

import users.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_address_options_remove_user_company_vat_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="timezone",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Asia/Ust-Nera", "Asia/Ust-Nera"),
                    ("Etc/GMT-11", "Etc/GMT-11"),
                    ("Asia/Kabul", "Asia/Kabul"),
                    ("Atlantic/Stanley", "Atlantic/Stanley"),
                    ("Africa/Luanda", "Africa/Luanda"),
                    ("Africa/Bangui", "Africa/Bangui"),
                    ("Europe/Jersey", "Europe/Jersey"),
                    ("America/Grand_Turk", "America/Grand_Turk"),
                    ("America/Goose_Bay", "America/Goose_Bay"),
                    ("Antarctica/Vostok", "Antarctica/Vostok"),
                    ("Asia/Ulaanbaatar", "Asia/Ulaanbaatar"),
                    ("Pacific/Saipan", "Pacific/Saipan"),
                    ("America/Recife", "America/Recife"),
                    ("America/Aruba", "America/Aruba"),
                    ("America/Porto_Acre", "America/Porto_Acre"),
                    ("America/Toronto", "America/Toronto"),
                    ("Africa/Lusaka", "Africa/Lusaka"),
                    ("Asia/Atyrau", "Asia/Atyrau"),
                    ("CET", "CET"),
                    ("Pacific/Galapagos", "Pacific/Galapagos"),
                    ("Africa/Harare", "Africa/Harare"),
                    ("America/Iqaluit", "America/Iqaluit"),
                    ("America/Kentucky/Louisville", "America/Kentucky/Louisville"),
                    ("Asia/Tashkent", "Asia/Tashkent"),
                    ("America/Managua", "America/Managua"),
                    ("America/Jamaica", "America/Jamaica"),
                    ("Africa/Asmara", "Africa/Asmara"),
                    ("America/Chihuahua", "America/Chihuahua"),
                    ("Pacific/Wake", "Pacific/Wake"),
                    ("America/St_Thomas", "America/St_Thomas"),
                    ("Pacific/Fakaofo", "Pacific/Fakaofo"),
                    ("America/Miquelon", "America/Miquelon"),
                    ("Pacific/Samoa", "Pacific/Samoa"),
                    ("Pacific/Chuuk", "Pacific/Chuuk"),
                    ("Indian/Reunion", "Indian/Reunion"),
                    ("Africa/Niamey", "Africa/Niamey"),
                    ("America/Antigua", "America/Antigua"),
                    ("Europe/Gibraltar", "Europe/Gibraltar"),
                    ("America/St_Johns", "America/St_Johns"),
                    ("Etc/GMT-2", "Etc/GMT-2"),
                    ("Europe/Kirov", "Europe/Kirov"),
                    ("Etc/GMT-10", "Etc/GMT-10"),
                    ("Australia/Lindeman", "Australia/Lindeman"),
                    ("Africa/Kigali", "Africa/Kigali"),
                    ("America/Indiana/Tell_City", "America/Indiana/Tell_City"),
                    ("America/Panama", "America/Panama"),
                    ("Etc/GMT+11", "Etc/GMT+11"),
                    ("Africa/Khartoum", "Africa/Khartoum"),
                    ("Asia/Makassar", "Asia/Makassar"),
                    ("Etc/GMT-7", "Etc/GMT-7"),
                    ("America/St_Kitts", "America/St_Kitts"),
                    ("Europe/Ulyanovsk", "Europe/Ulyanovsk"),
                    ("America/Cuiaba", "America/Cuiaba"),
                    ("Africa/Blantyre", "Africa/Blantyre"),
                    ("Europe/Volgograd", "Europe/Volgograd"),
                    ("Africa/Accra", "Africa/Accra"),
                    ("Europe/Saratov", "Europe/Saratov"),
                    ("America/Rainy_River", "America/Rainy_River"),
                    ("Indian/Kerguelen", "Indian/Kerguelen"),
                    ("Etc/Zulu", "Etc/Zulu"),
                    ("Africa/Nairobi", "Africa/Nairobi"),
                    ("America/Whitehorse", "America/Whitehorse"),
                    ("America/Lower_Princes", "America/Lower_Princes"),
                    ("Etc/GMT-1", "Etc/GMT-1"),
                    ("Africa/Porto-Novo", "Africa/Porto-Novo"),
                    ("Europe/Monaco", "Europe/Monaco"),
                    ("America/Asuncion", "America/Asuncion"),
                    ("Pacific/Gambier", "Pacific/Gambier"),
                    ("Pacific/Easter", "Pacific/Easter"),
                    ("America/Creston", "America/Creston"),
                    ("Europe/Oslo", "Europe/Oslo"),
                    ("America/Caracas", "America/Caracas"),
                    ("America/Los_Angeles", "America/Los_Angeles"),
                    ("America/Thunder_Bay", "America/Thunder_Bay"),
                    ("Etc/GMT+1", "Etc/GMT+1"),
                    ("Europe/Athens", "Europe/Athens"),
                    ("Europe/Dublin", "Europe/Dublin"),
                    ("Africa/Addis_Ababa", "Africa/Addis_Ababa"),
                    ("Atlantic/Cape_Verde", "Atlantic/Cape_Verde"),
                    ("Asia/Vladivostok", "Asia/Vladivostok"),
                    ("Africa/Algiers", "Africa/Algiers"),
                    ("Africa/Timbuktu", "Africa/Timbuktu"),
                    ("America/Santarem", "America/Santarem"),
                    ("Europe/Vilnius", "Europe/Vilnius"),
                    ("Africa/Mogadishu", "Africa/Mogadishu"),
                    ("Asia/Kamchatka", "Asia/Kamchatka"),
                    ("Antarctica/Davis", "Antarctica/Davis"),
                    ("America/Scoresbysund", "America/Scoresbysund"),
                    ("Europe/Tallinn", "Europe/Tallinn"),
                    ("Europe/Mariehamn", "Europe/Mariehamn"),
                    ("Asia/Bishkek", "Asia/Bishkek"),
                    ("Pacific/Funafuti", "Pacific/Funafuti"),
                    ("America/Swift_Current", "America/Swift_Current"),
                    ("Indian/Antananarivo", "Indian/Antananarivo"),
                    ("America/Dawson_Creek", "America/Dawson_Creek"),
                    ("Africa/Maseru", "Africa/Maseru"),
                    ("Europe/Bucharest", "Europe/Bucharest"),
                    ("Asia/Hovd", "Asia/Hovd"),
                    ("America/Danmarkshavn", "America/Danmarkshavn"),
                    ("localtime", "localtime"),
                    ("Europe/Madrid", "Europe/Madrid"),
                    ("America/Edmonton", "America/Edmonton"),
                    ("Pacific/Kosrae", "Pacific/Kosrae"),
                    ("Africa/Douala", "Africa/Douala"),
                    ("America/Cancun", "America/Cancun"),
                    ("Africa/Lagos", "Africa/Lagos"),
                    ("America/Guyana", "America/Guyana"),
                    ("America/Argentina/Tucuman", "America/Argentina/Tucuman"),
                    ("Pacific/Rarotonga", "Pacific/Rarotonga"),
                    ("Asia/Irkutsk", "Asia/Irkutsk"),
                    ("Etc/GMT+8", "Etc/GMT+8"),
                    ("Europe/Prague", "Europe/Prague"),
                    ("America/North_Dakota/New_Salem", "America/North_Dakota/New_Salem"),
                    ("Asia/Hebron", "Asia/Hebron"),
                    ("America/Port-au-Prince", "America/Port-au-Prince"),
                    ("Factory", "Factory"),
                    ("Pacific/Honolulu", "Pacific/Honolulu"),
                    ("America/Hermosillo", "America/Hermosillo"),
                    ("Africa/Ceuta", "Africa/Ceuta"),
                    ("UTC", "UTC"),
                    ("Asia/Jakarta", "Asia/Jakarta"),
                    ("Pacific/Kiritimati", "Pacific/Kiritimati"),
                    ("Etc/GMT-0", "Etc/GMT-0"),
                    ("Etc/GMT+9", "Etc/GMT+9"),
                    ("Asia/Omsk", "Asia/Omsk"),
                    ("Pacific/Fiji", "Pacific/Fiji"),
                    ("America/Grenada", "America/Grenada"),
                    ("Asia/Muscat", "Asia/Muscat"),
                    ("Africa/Windhoek", "Africa/Windhoek"),
                    ("Europe/Simferopol", "Europe/Simferopol"),
                    ("Asia/Macau", "Asia/Macau"),
                    ("Etc/GMT+3", "Etc/GMT+3"),
                    ("Europe/Paris", "Europe/Paris"),
                    ("Asia/Baku", "Asia/Baku"),
                    ("Asia/Samarkand", "Asia/Samarkand"),
                    ("America/New_York", "America/New_York"),
                    ("Africa/Banjul", "Africa/Banjul"),
                    ("Asia/Dhaka", "Asia/Dhaka"),
                    ("Asia/Shanghai", "Asia/Shanghai"),
                    ("Asia/Sakhalin", "Asia/Sakhalin"),
                    ("Asia/Jerusalem", "Asia/Jerusalem"),
                    ("America/Phoenix", "America/Phoenix"),
                    ("Australia/Perth", "Australia/Perth"),
                    ("Asia/Choibalsan", "Asia/Choibalsan"),
                    ("Asia/Pontianak", "Asia/Pontianak"),
                    ("Europe/Moscow", "Europe/Moscow"),
                    ("Africa/Lome", "Africa/Lome"),
                    ("Etc/GMT+5", "Etc/GMT+5"),
                    ("America/Yellowknife", "America/Yellowknife"),
                    ("Etc/UCT", "Etc/UCT"),
                    ("America/Ciudad_Juarez", "America/Ciudad_Juarez"),
                    ("Etc/GMT+12", "Etc/GMT+12"),
                    ("Europe/Astrakhan", "Europe/Astrakhan"),
                    ("Africa/Monrovia", "Africa/Monrovia"),
                    ("Europe/Rome", "Europe/Rome"),
                    ("Asia/Tel_Aviv", "Asia/Tel_Aviv"),
                    ("America/Halifax", "America/Halifax"),
                    ("America/Denver", "America/Denver"),
                    ("Etc/UTC", "Etc/UTC"),
                    ("Europe/Helsinki", "Europe/Helsinki"),
                    ("America/Argentina/San_Juan", "America/Argentina/San_Juan"),
                    ("America/Monterrey", "America/Monterrey"),
                    ("Asia/Dubai", "Asia/Dubai"),
                    ("America/Montserrat", "America/Montserrat"),
                    ("America/Indiana/Indianapolis", "America/Indiana/Indianapolis"),
                    ("America/Atka", "America/Atka"),
                    ("Asia/Hong_Kong", "Asia/Hong_Kong"),
                    ("America/Menominee", "America/Menominee"),
                    ("Asia/Nicosia", "Asia/Nicosia"),
                    ("Europe/Vienna", "Europe/Vienna"),
                    ("CST6CDT", "CST6CDT"),
                    ("America/Bogota", "America/Bogota"),
                    ("Atlantic/Madeira", "Atlantic/Madeira"),
                    ("Africa/Cairo", "Africa/Cairo"),
                    ("America/St_Barthelemy", "America/St_Barthelemy"),
                    ("Africa/Conakry", "Africa/Conakry"),
                    ("Pacific/Wallis", "Pacific/Wallis"),
                    ("Etc/Greenwich", "Etc/Greenwich"),
                    ("Africa/Nouakchott", "Africa/Nouakchott"),
                    ("America/Santa_Isabel", "America/Santa_Isabel"),
                    ("America/Puerto_Rico", "America/Puerto_Rico"),
                    ("Europe/Vaduz", "Europe/Vaduz"),
                    ("Africa/Djibouti", "Africa/Djibouti"),
                    ("America/Tortola", "America/Tortola"),
                    ("Asia/Chongqing", "Asia/Chongqing"),
                    ("Asia/Singapore", "Asia/Singapore"),
                    ("Africa/Bujumbura", "Africa/Bujumbura"),
                    ("Africa/Kampala", "Africa/Kampala"),
                    ("Etc/GMT-4", "Etc/GMT-4"),
                    ("Asia/Colombo", "Asia/Colombo"),
                    ("Asia/Chita", "Asia/Chita"),
                    ("America/Regina", "America/Regina"),
                    ("America/Dawson", "America/Dawson"),
                    ("Asia/Tokyo", "Asia/Tokyo"),
                    ("America/Cambridge_Bay", "America/Cambridge_Bay"),
                    ("Australia/Adelaide", "Australia/Adelaide"),
                    ("Etc/GMT-14", "Etc/GMT-14"),
                    ("Pacific/Efate", "Pacific/Efate"),
                    ("America/Porto_Velho", "America/Porto_Velho"),
                    ("America/Curacao", "America/Curacao"),
                    ("America/Thule", "America/Thule"),
                    ("Atlantic/South_Georgia", "Atlantic/South_Georgia"),
                    ("America/Rankin_Inlet", "America/Rankin_Inlet"),
                    ("America/Rio_Branco", "America/Rio_Branco"),
                    ("Indian/Mayotte", "Indian/Mayotte"),
                    ("Asia/Ashgabat", "Asia/Ashgabat"),
                    ("Antarctica/Troll", "Antarctica/Troll"),
                    ("Asia/Urumqi", "Asia/Urumqi"),
                    ("Australia/Darwin", "Australia/Darwin"),
                    ("Pacific/Auckland", "Pacific/Auckland"),
                    ("Asia/Tbilisi", "Asia/Tbilisi"),
                    ("America/Indiana/Knox", "America/Indiana/Knox"),
                    ("Asia/Seoul", "Asia/Seoul"),
                    ("Indian/Comoro", "Indian/Comoro"),
                    ("America/Fort_Nelson", "America/Fort_Nelson"),
                    ("Asia/Bangkok", "Asia/Bangkok"),
                    ("Europe/Copenhagen", "Europe/Copenhagen"),
                    ("Asia/Taipei", "Asia/Taipei"),
                    ("Africa/Tunis", "Africa/Tunis"),
                    ("Africa/El_Aaiun", "Africa/El_Aaiun"),
                    ("America/Metlakatla", "America/Metlakatla"),
                    ("Antarctica/Macquarie", "Antarctica/Macquarie"),
                    ("Etc/GMT+4", "Etc/GMT+4"),
                    ("Etc/GMT-5", "Etc/GMT-5"),
                    ("America/North_Dakota/Center", "America/North_Dakota/Center"),
                    ("MET", "MET"),
                    ("Europe/Samara", "Europe/Samara"),
                    ("Asia/Almaty", "Asia/Almaty"),
                    ("Indian/Mauritius", "Indian/Mauritius"),
                    ("Europe/Andorra", "Europe/Andorra"),
                    ("Etc/GMT0", "Etc/GMT0"),
                    ("Africa/Gaborone", "Africa/Gaborone"),
                    ("America/Atikokan", "America/Atikokan"),
                    ("Pacific/Pitcairn", "Pacific/Pitcairn"),
                    ("Pacific/Niue", "Pacific/Niue"),
                    ("America/Inuvik", "America/Inuvik"),
                    ("Asia/Aden", "Asia/Aden"),
                    ("Europe/Istanbul", "Europe/Istanbul"),
                    ("Asia/Novokuznetsk", "Asia/Novokuznetsk"),
                    ("Asia/Tehran", "Asia/Tehran"),
                    ("Asia/Ho_Chi_Minh", "Asia/Ho_Chi_Minh"),
                    ("Africa/Ndjamena", "Africa/Ndjamena"),
                    ("America/Marigot", "America/Marigot"),
                    ("Etc/GMT-12", "Etc/GMT-12"),
                    ("Asia/Magadan", "Asia/Magadan"),
                    ("America/El_Salvador", "America/El_Salvador"),
                    ("Asia/Krasnoyarsk", "Asia/Krasnoyarsk"),
                    ("America/Indiana/Vincennes", "America/Indiana/Vincennes"),
                    ("America/Matamoros", "America/Matamoros"),
                    ("America/Montreal", "America/Montreal"),
                    ("Antarctica/Palmer", "Antarctica/Palmer"),
                    ("Antarctica/DumontDUrville", "Antarctica/DumontDUrville"),
                    ("America/Argentina/Ushuaia", "America/Argentina/Ushuaia"),
                    ("Pacific/Noumea", "Pacific/Noumea"),
                    ("Europe/Sarajevo", "Europe/Sarajevo"),
                    ("America/Coral_Harbour", "America/Coral_Harbour"),
                    ("Etc/GMT-13", "Etc/GMT-13"),
                    ("Europe/Malta", "Europe/Malta"),
                    ("Pacific/Tongatapu", "Pacific/Tongatapu"),
                    ("Africa/Juba", "Africa/Juba"),
                    ("Australia/Yancowinna", "Australia/Yancowinna"),
                    ("Pacific/Marquesas", "Pacific/Marquesas"),
                    ("Europe/Podgorica", "Europe/Podgorica"),
                    ("America/Chicago", "America/Chicago"),
                    ("Pacific/Port_Moresby", "Pacific/Port_Moresby"),
                    ("Europe/Bratislava", "Europe/Bratislava"),
                    ("Pacific/Palau", "Pacific/Palau"),
                    ("Asia/Yangon", "Asia/Yangon"),
                    ("Indian/Christmas", "Indian/Christmas"),
                    ("America/Argentina/Rio_Gallegos", "America/Argentina/Rio_Gallegos"),
                    ("America/Indiana/Petersburg", "America/Indiana/Petersburg"),
                    ("America/St_Lucia", "America/St_Lucia"),
                    ("Pacific/Nauru", "Pacific/Nauru"),
                    ("Antarctica/Rothera", "Antarctica/Rothera"),
                    ("Asia/Aqtau", "Asia/Aqtau"),
                    ("Africa/Bamako", "Africa/Bamako"),
                    ("America/Belem", "America/Belem"),
                    ("Europe/Warsaw", "Europe/Warsaw"),
                    ("Asia/Kashgar", "Asia/Kashgar"),
                    ("America/Belize", "America/Belize"),
                    ("America/Anguilla", "America/Anguilla"),
                    ("Pacific/Tahiti", "Pacific/Tahiti"),
                    ("Australia/Sydney", "Australia/Sydney"),
                    ("America/Merida", "America/Merida"),
                    ("America/St_Vincent", "America/St_Vincent"),
                    ("America/Blanc-Sablon", "America/Blanc-Sablon"),
                    ("America/North_Dakota/Beulah", "America/North_Dakota/Beulah"),
                    ("Europe/San_Marino", "Europe/San_Marino"),
                    ("Africa/Malabo", "Africa/Malabo"),
                    ("America/Lima", "America/Lima"),
                    ("Australia/Broken_Hill", "Australia/Broken_Hill"),
                    ("America/Sitka", "America/Sitka"),
                    ("America/Port_of_Spain", "America/Port_of_Spain"),
                    ("Asia/Brunei", "Asia/Brunei"),
                    ("Europe/Kyiv", "Europe/Kyiv"),
                    ("Asia/Pyongyang", "Asia/Pyongyang"),
                    ("America/Mazatlan", "America/Mazatlan"),
                    ("America/Juneau", "America/Juneau"),
                    ("Asia/Kuala_Lumpur", "Asia/Kuala_Lumpur"),
                    ("America/Virgin", "America/Virgin"),
                    ("Asia/Dushanbe", "Asia/Dushanbe"),
                    ("Europe/Tiraspol", "Europe/Tiraspol"),
                    ("America/Eirunepe", "America/Eirunepe"),
                    ("Europe/Sofia", "Europe/Sofia"),
                    ("Asia/Barnaul", "Asia/Barnaul"),
                    ("Europe/Stockholm", "Europe/Stockholm"),
                    ("Europe/Guernsey", "Europe/Guernsey"),
                    ("HST", "HST"),
                    ("America/Bahia_Banderas", "America/Bahia_Banderas"),
                    ("Africa/Johannesburg", "Africa/Johannesburg"),
                    ("America/Maceio", "America/Maceio"),
                    ("America/Argentina/Buenos_Aires", "America/Argentina/Buenos_Aires"),
                    ("America/Argentina/Jujuy", "America/Argentina/Jujuy"),
                    ("Asia/Karachi", "Asia/Karachi"),
                    ("America/Ensenada", "America/Ensenada"),
                    ("Africa/Mbabane", "Africa/Mbabane"),
                    ("America/Barbados", "America/Barbados"),
                    ("Indian/Mahe", "Indian/Mahe"),
                    ("Europe/Tirane", "Europe/Tirane"),
                    ("Europe/Zagreb", "Europe/Zagreb"),
                    ("Arctic/Longyearbyen", "Arctic/Longyearbyen"),
                    ("Africa/Maputo", "Africa/Maputo"),
                    ("America/Fortaleza", "America/Fortaleza"),
                    ("Asia/Istanbul", "Asia/Istanbul"),
                    ("America/Indiana/Winamac", "America/Indiana/Winamac"),
                    ("Asia/Kathmandu", "Asia/Kathmandu"),
                    ("America/Winnipeg", "America/Winnipeg"),
                    ("GMT", "GMT"),
                    ("Asia/Khandyga", "Asia/Khandyga"),
                    ("Europe/Nicosia", "Europe/Nicosia"),
                    ("America/Montevideo", "America/Montevideo"),
                    ("Pacific/Yap", "Pacific/Yap"),
                    ("Asia/Tomsk", "Asia/Tomsk"),
                    ("America/Pangnirtung", "America/Pangnirtung"),
                    ("Australia/Eucla", "Australia/Eucla"),
                    ("Asia/Dili", "Asia/Dili"),
                    ("Africa/Dakar", "Africa/Dakar"),
                    ("Pacific/Kwajalein", "Pacific/Kwajalein"),
                    ("Europe/Riga", "Europe/Riga"),
                    ("Africa/Abidjan", "Africa/Abidjan"),
                    ("America/Nassau", "America/Nassau"),
                    ("Europe/Chisinau", "Europe/Chisinau"),
                    ("Pacific/Kanton", "Pacific/Kanton"),
                    ("Africa/Ouagadougou", "Africa/Ouagadougou"),
                    ("Africa/Lubumbashi", "Africa/Lubumbashi"),
                    ("Asia/Kuwait", "Asia/Kuwait"),
                    ("Etc/GMT+2", "Etc/GMT+2"),
                    ("PST8PDT", "PST8PDT"),
                    ("Etc/GMT+6", "Etc/GMT+6"),
                    ("Europe/Budapest", "Europe/Budapest"),
                    ("America/Yakutat", "America/Yakutat"),
                    ("America/La_Paz", "America/La_Paz"),
                    ("Asia/Qyzylorda", "Asia/Qyzylorda"),
                    ("Europe/Brussels", "Europe/Brussels"),
                    ("WET", "WET"),
                    ("America/Argentina/Salta", "America/Argentina/Salta"),
                    ("Atlantic/Azores", "Atlantic/Azores"),
                    ("Africa/Libreville", "Africa/Libreville"),
                    ("America/Mexico_City", "America/Mexico_City"),
                    ("MST7MDT", "MST7MDT"),
                    ("America/Guadeloupe", "America/Guadeloupe"),
                    ("Asia/Yekaterinburg", "Asia/Yekaterinburg"),
                    ("America/Punta_Arenas", "America/Punta_Arenas"),
                    ("Africa/Tripoli", "Africa/Tripoli"),
                    ("Asia/Thimphu", "Asia/Thimphu"),
                    ("Asia/Gaza", "Asia/Gaza"),
                    ("Atlantic/Reykjavik", "Atlantic/Reykjavik"),
                    ("Europe/Ljubljana", "Europe/Ljubljana"),
                    ("America/Detroit", "America/Detroit"),
                    ("America/Cayman", "America/Cayman"),
                    ("Pacific/Pohnpei", "Pacific/Pohnpei"),
                    ("America/Anchorage", "America/Anchorage"),
                    ("America/Bahia", "America/Bahia"),
                    ("Indian/Maldives", "Indian/Maldives"),
                    ("Europe/London", "Europe/London"),
                    ("America/Araguaina", "America/Araguaina"),
                    ("America/Kralendijk", "America/Kralendijk"),
                    ("Europe/Minsk", "Europe/Minsk"),
                    ("Australia/Lord_Howe", "Australia/Lord_Howe"),
                    ("America/Noronha", "America/Noronha"),
                    ("Africa/Bissau", "Africa/Bissau"),
                    ("America/Guatemala", "America/Guatemala"),
                    ("Pacific/Majuro", "Pacific/Majuro"),
                    ("Europe/Berlin", "Europe/Berlin"),
                    ("Asia/Aqtobe", "Asia/Aqtobe"),
                    ("Pacific/Guadalcanal", "Pacific/Guadalcanal"),
                    ("Etc/GMT-6", "Etc/GMT-6"),
                    ("Antarctica/Casey", "Antarctica/Casey"),
                    ("Africa/Dar_es_Salaam", "Africa/Dar_es_Salaam"),
                    ("America/Cayenne", "America/Cayenne"),
                    ("Etc/Universal", "Etc/Universal"),
                    ("America/Adak", "America/Adak"),
                    ("Etc/GMT-8", "Etc/GMT-8"),
                    ("America/Nuuk", "America/Nuuk"),
                    ("Asia/Bahrain", "Asia/Bahrain"),
                    ("Africa/Sao_Tome", "Africa/Sao_Tome"),
                    ("Africa/Casablanca", "Africa/Casablanca"),
                    ("Australia/Currie", "Australia/Currie"),
                    ("Atlantic/Bermuda", "Atlantic/Bermuda"),
                    ("Etc/GMT-9", "Etc/GMT-9"),
                    ("America/Tegucigalpa", "America/Tegucigalpa"),
                    ("America/Costa_Rica", "America/Costa_Rica"),
                    ("Asia/Manila", "Asia/Manila"),
                    ("Asia/Amman", "Asia/Amman"),
                    ("Asia/Yakutsk", "Asia/Yakutsk"),
                    ("Pacific/Pago_Pago", "Pacific/Pago_Pago"),
                    ("Indian/Cocos", "Indian/Cocos"),
                    ("Etc/GMT+10", "Etc/GMT+10"),
                    ("Asia/Yerevan", "Asia/Yerevan"),
                    ("EST5EDT", "EST5EDT"),
                    ("Etc/GMT", "Etc/GMT"),
                    ("Atlantic/Canary", "Atlantic/Canary"),
                    ("Asia/Qatar", "Asia/Qatar"),
                    ("Pacific/Norfolk", "Pacific/Norfolk"),
                    ("Pacific/Midway", "Pacific/Midway"),
                    ("Australia/Hobart", "Australia/Hobart"),
                    ("Europe/Belfast", "Europe/Belfast"),
                    ("America/Boise", "America/Boise"),
                    ("Asia/Jayapura", "Asia/Jayapura"),
                    ("Etc/GMT+0", "Etc/GMT+0"),
                    ("America/Ojinaga", "America/Ojinaga"),
                    ("America/Nipigon", "America/Nipigon"),
                    ("America/Indiana/Vevay", "America/Indiana/Vevay"),
                    ("Australia/Canberra", "Australia/Canberra"),
                    ("Pacific/Johnston", "Pacific/Johnston"),
                    ("Atlantic/St_Helena", "Atlantic/St_Helena"),
                    ("America/Martinique", "America/Martinique"),
                    ("Africa/Brazzaville", "Africa/Brazzaville"),
                    ("Antarctica/McMurdo", "Antarctica/McMurdo"),
                    ("America/Manaus", "America/Manaus"),
                    ("EST", "EST"),
                    ("Asia/Qostanay", "Asia/Qostanay"),
                    ("EET", "EET"),
                    ("America/Boa_Vista", "America/Boa_Vista"),
                    ("Etc/GMT-3", "Etc/GMT-3"),
                    ("Asia/Kolkata", "Asia/Kolkata"),
                    ("Europe/Busingen", "Europe/Busingen"),
                    ("Atlantic/Jan_Mayen", "Atlantic/Jan_Mayen"),
                    ("Europe/Luxembourg", "Europe/Luxembourg"),
                    ("Europe/Vatican", "Europe/Vatican"),
                    ("Pacific/Guam", "Pacific/Guam"),
                    ("MST", "MST"),
                    ("Asia/Anadyr", "Asia/Anadyr"),
                    ("America/Vancouver", "America/Vancouver"),
                    ("Africa/Kinshasa", "Africa/Kinshasa"),
                    ("Europe/Zurich", "Europe/Zurich"),
                    ("Asia/Oral", "Asia/Oral"),
                    ("America/Argentina/Mendoza", "America/Argentina/Mendoza"),
                    ("America/Shiprock", "America/Shiprock"),
                    ("Atlantic/Faroe", "Atlantic/Faroe"),
                    ("Asia/Baghdad", "Asia/Baghdad"),
                    ("America/Campo_Grande", "America/Campo_Grande"),
                    ("America/Argentina/Cordoba", "America/Argentina/Cordoba"),
                    ("America/Sao_Paulo", "America/Sao_Paulo"),
                    ("America/Dominica", "America/Dominica"),
                    ("America/Kentucky/Monticello", "America/Kentucky/Monticello"),
                    ("America/Tijuana", "America/Tijuana"),
                    ("America/Santo_Domingo", "America/Santo_Domingo"),
                    ("America/Santiago", "America/Santiago"),
                    ("America/Guayaquil", "America/Guayaquil"),
                    ("America/Resolute", "America/Resolute"),
                    ("Asia/Harbin", "Asia/Harbin"),
                    ("Europe/Lisbon", "Europe/Lisbon"),
                    ("Antarctica/Syowa", "Antarctica/Syowa"),
                    ("Asia/Kuching", "Asia/Kuching"),
                    ("Asia/Riyadh", "Asia/Riyadh"),
                    ("Europe/Belgrade", "Europe/Belgrade"),
                    ("Indian/Chagos", "Indian/Chagos"),
                    ("America/Paramaribo", "America/Paramaribo"),
                    ("Asia/Srednekolymsk", "Asia/Srednekolymsk"),
                    ("America/Indiana/Marengo", "America/Indiana/Marengo"),
                    ("Asia/Beirut", "Asia/Beirut"),
                    ("Asia/Vientiane", "Asia/Vientiane"),
                    ("Asia/Phnom_Penh", "Asia/Phnom_Penh"),
                    ("Australia/Melbourne", "Australia/Melbourne"),
                    ("Pacific/Chatham", "Pacific/Chatham"),
                    ("Asia/Novosibirsk", "Asia/Novosibirsk"),
                    ("Etc/GMT+7", "Etc/GMT+7"),
                    ("Pacific/Apia", "Pacific/Apia"),
                    ("Europe/Amsterdam", "Europe/Amsterdam"),
                    ("Asia/Famagusta", "Asia/Famagusta"),
                    ("Asia/Damascus", "Asia/Damascus"),
                    ("America/Nome", "America/Nome"),
                    ("America/Argentina/Catamarca", "America/Argentina/Catamarca"),
                    ("America/Moncton", "America/Moncton"),
                    ("Europe/Skopje", "Europe/Skopje"),
                    ("Australia/Brisbane", "Australia/Brisbane"),
                    ("Antarctica/Mawson", "Antarctica/Mawson"),
                    ("Europe/Kaliningrad", "Europe/Kaliningrad"),
                    ("America/Argentina/San_Luis", "America/Argentina/San_Luis"),
                    ("Pacific/Tarawa", "Pacific/Tarawa"),
                    ("Europe/Isle_of_Man", "Europe/Isle_of_Man"),
                    ("Pacific/Bougainville", "Pacific/Bougainville"),
                    ("America/Havana", "America/Havana"),
                    ("America/Glace_Bay", "America/Glace_Bay"),
                    ("Africa/Freetown", "Africa/Freetown"),
                    ("America/Argentina/La_Rioja", "America/Argentina/La_Rioja"),
                ],
                max_length=128,
                null=True,
                verbose_name="timezone",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="title",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Mr", "Mr"),
                    ("Mrs", "Mrs"),
                    ("Miss", "Miss"),
                    ("Ms", "Ms"),
                    ("Dr", "Dr"),
                    ("Prof", "Prof"),
                    ("Sir", "Sir"),
                ],
                default=users.enums.Titles["MR"],
                max_length=10,
                null=True,
                verbose_name="title",
            ),
        ),
    ]