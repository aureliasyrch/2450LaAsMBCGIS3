from flask import Blueprint, render_template, jsonify

maps_bp = Blueprint('maps', __name__)

lokasi = [
   {"latitude": -6.877807, "longitude": 107.587507,
     "name": "MUSEUM BARLI",
     "address": "JL. PROF. DR. SUTAMI NO. 91, BANDUNG"},

    {"latitude": -6.921034, "longitude": 107.577263,
     "name": "MUSEUM KEBUDAYAAN TIONGHOA",
     "address": "JL. NANA ROHANA NO. 37, BANDUNG"},
    
    {"latitude": -6.851163, "longitude": 107.596201,
     "name": "MUSEUM 3D",
     "address": "JL. DR. SETIABUDI, BANDUNG"},

    {"latitude": -6.920428, "longitude": 107.613571,
     "name": "MUSEUM WOLFF SCHOEMAKER (PREANGER)",
     "address": "JL. ASIA AFRIKA NO. 81, BANDUNG"},
   
    {"latitude": -6.909653, "longitude": 107.609532,
     "name": "MUSEUM KOTA BANDUNG",
     "address": "JL. ACEH NO. 47, BANDUNG"},
    
    {"latitude": -6.916771, "longitude": 107.611069,
     "name": "MUSEUM MANDALA WANGSIT SILIWANGI",
     "address": "JL. LEMBONG NO. 39, BANDUNG"},

    {"latitude": -6.937420, "longitude": 107.603531,
     "name": "MUSEUM SRI BADUGA",
     "address": "JL. BKR NO. 185, BANDUNG"},

    {"latitude": -6.900578, "longitude": 107.621434,
     "name": "MUSEUM GEOLOGI BANDUNG",
     "address": "JL. DIPONEGORO NO. 57, BANDUNG"},
  
    {"latitude": -6.902481232205368, "longitude": 107.61911326473744,
     "name": "MUSEUM GEDUNG SATE",
     "address": "JL. DIPONEGORO NO. 22, BANDUNG"},

    {"latitude": -6.920086, "longitude": 107.609756,
     "name": "MUSEUM KONFERENSI ASIA AFRIKA",
     "address": "JL. ASIA AFRIKA NO. 65, BANDUNG"},
   
    {"latitude": -6.901838, "longitude": 107.619712,
     "name": "MUSEUM POS INDONESIA",
     "address": "JL. CILAKI NO. 73, BANDUNG"},
    
    {"latitude": -6.918883, "longitude": 107.607094,
     "name": "MUSEUM LAPAS BANCEUY",
     "address": "JL. BANCEUY, BANDUNG"},

    {"latitude": -6.919912, "longitude": 107.617656,
     "name": "MUSEUM MAINAN",
     "address": "JL. SUNDA NO. 39, BANDUNG"},
   
    {"latitude": -6.926888, "longitude": 107.628344,
     "name": "MUSEUM VIRAJATI SESKOAD",
     "address": "JL. GATOT SUBROTO NO. 96, BANDUNG"},
    
    {"latitude": -6.939813, "longitude": 107.672661,
     "name": "MUSEUM NIKE ARDILLA",
     "address": "KOMP. ARYA GRAHA. JL. ARIA UTAMA NO. 5, BANDUNG"},

    {"latitude": -6.935419, "longitude": 107.662201,
     "name": "HALL OF FAME JAWA BARAT - PANGGUNG INOHONG",
     "address": "BAPUSIPDA, BANDUNG"},
   
    {"latitude": -6.859631308549626, "longitude": 107.59418501022243,
     "name": "MUSEUM PENDIDIKAN NASIONAL",
     "address": "JL. DR. SETIABUDI NO. 225, BANDUNG"},
    
    {"latitude": -6.913399, "longitude": 107.608023,
     "name": "GEDUNG INDONESIA MENGGUGAT",
     "address": "JL. PERINTIS KEMERDEKAAN NO. 5, BANDUNG"},

    {"latitude": -6.893177, "longitude": 107.618498,
     "name": "MUSEUM PERJUANGAN RAKYAT JAWA BARAT",
     "address": "JL. DIPATIUKUR NO. 48, BANDUNG"},
    
    {"latitude": -6.876038, "longitude": 107.572717,
     "name": "NUART SCULPTURE PARK",
     "address": "SETARA DUTA RAYA NO. L6, CIWARUGA, BANDUNG"}

]

@maps_bp.route('/lokasi')
def lokasi_view():
    return jsonify(lokasi)

@maps_bp.route('/maps')
def maps():
    return render_template('maps.html')