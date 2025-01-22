from gcn_kafka import Consumer
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
# Environment variables
GCN_KAFKA_CLIENT = os.getenv("GCN_KAFKA_CLIENT")
GCN_KAFKA_SECRET = os.getenv("GCN_KAFKA_SECRET")

# Connect as a consumer (client "tracet")
# Warning: don't share the client secret with others.
consumer = Consumer(client_id=GCN_KAFKA_CLIENT, client_secret=GCN_KAFKA_SECRET)

# Subscribe to topics and receive alerts
consumer.subscribe(
    [
        # "gcn.classic.voevent.AGILE_GRB_GROUND",
        "gcn.classic.voevent.AGILE_GRB_POS_TEST",
        # "gcn.classic.voevent.AGILE_GRB_REFINED",
        # "gcn.classic.voevent.AGILE_GRB_WAKEUP",
        "gcn.classic.voevent.AGILE_MCAL_ALERT",
        # "gcn.classic.voevent.AGILE_POINTDIR",
        # "gcn.classic.voevent.AGILE_TRANS",
        # "gcn.classic.voevent.AMON_ICECUBE_COINC",
        # "gcn.classic.voevent.AMON_ICECUBE_EHE",
        # "gcn.classic.voevent.AMON_ICECUBE_HESE",
        "gcn.classic.voevent.AMON_NU_EM_COINC",
        "gcn.classic.voevent.CALET_GBM_FLT_LC",
        # "gcn.classic.voevent.CALET_GBM_GND_LC",
        "gcn.classic.voevent.FERMI_GBM_ALERT",
        "gcn.classic.voevent.FERMI_GBM_FIN_POS",
        "gcn.classic.voevent.FERMI_GBM_FLT_POS",
        "gcn.classic.voevent.FERMI_GBM_GND_POS",
        # "gcn.classic.voevent.FERMI_GBM_LC",
        "gcn.classic.voevent.FERMI_GBM_POS_TEST",
        "gcn.classic.voevent.FERMI_GBM_SUBTHRESH",
        # "gcn.classic.voevent.FERMI_GBM_TRANS",
        # "gcn.classic.voevent.FERMI_LAT_GND",
        "gcn.classic.voevent.FERMI_LAT_MONITOR",
        "gcn.classic.voevent.FERMI_LAT_OFFLINE",
        # "gcn.classic.voevent.FERMI_LAT_POS_DIAG",
        # "gcn.classic.voevent.FERMI_LAT_POS_INI",
        "gcn.classic.voevent.FERMI_LAT_POS_TEST",
        # "gcn.classic.voevent.FERMI_LAT_POS_UPD",
        # "gcn.classic.voevent.FERMI_LAT_TRANS",
        "gcn.classic.voevent.FERMI_POINTDIR",
        # "gcn.classic.voevent.FERMI_SC_SLEW",
        "gcn.classic.voevent.GECAM_FLT",
        "gcn.classic.voevent.GECAM_GND",
        "gcn.classic.voevent.ICECUBE_ASTROTRACK_BRONZE",
        "gcn.classic.voevent.ICECUBE_ASTROTRACK_GOLD",
        "gcn.classic.voevent.ICECUBE_CASCADE",
        "gcn.classic.voevent.INTEGRAL_OFFLINE",
        "gcn.classic.voevent.INTEGRAL_POINTDIR",
        "gcn.classic.voevent.INTEGRAL_REFINED",
        "gcn.classic.voevent.INTEGRAL_SPIACS",
        "gcn.classic.voevent.INTEGRAL_WAKEUP",
        "gcn.classic.voevent.INTEGRAL_WEAK",
        # "gcn.classic.voevent.IPN_POS",
        "gcn.classic.voevent.IPN_RAW",
        # "gcn.classic.voevent.IPN_SEG",
        "gcn.classic.voevent.LVC_COUNTERPART",
        "gcn.classic.voevent.LVC_EARLY_WARNING",
        "gcn.classic.voevent.LVC_INITIAL",
        "gcn.classic.voevent.LVC_PRELIMINARY",
        "gcn.classic.voevent.LVC_RETRACTION",
        # "gcn.classic.voevent.LVC_TEST",
        "gcn.classic.voevent.LVC_UPDATE",
        "gcn.classic.voevent.MAXI_KNOWN",
        "gcn.classic.voevent.MAXI_TEST",
        "gcn.classic.voevent.MAXI_UNKNOWN",
        "gcn.classic.voevent.SWIFT_ACTUAL_POINTDIR",
        # "gcn.classic.voevent.SWIFT_BAT_ALARM_LONG",
        # "gcn.classic.voevent.SWIFT_BAT_ALARM_SHORT",
        # "gcn.classic.voevent.SWIFT_BAT_GRB_ALERT",
        "gcn.classic.voevent.SWIFT_BAT_GRB_LC",
        # "gcn.classic.voevent.SWIFT_BAT_GRB_LC_PROC",
        "gcn.classic.voevent.SWIFT_BAT_GRB_POS_ACK",
        # "gcn.classic.voevent.SWIFT_BAT_GRB_POS_NACK",
        "gcn.classic.voevent.SWIFT_BAT_GRB_POS_TEST",
        # "gcn.classic.voevent.SWIFT_BAT_KNOWN_SRC",
        # "gcn.classic.voevent.SWIFT_BAT_MONITOR",
        "gcn.classic.voevent.SWIFT_BAT_QL_POS",
        "gcn.classic.voevent.SWIFT_BAT_SCALEDMAP",
        # "gcn.classic.voevent.SWIFT_BAT_SLEW_POS",
        # "gcn.classic.voevent.SWIFT_BAT_SUB_THRESHOLD",
        # "gcn.classic.voevent.SWIFT_BAT_SUBSUB",
        "gcn.classic.voevent.SWIFT_BAT_TRANS",
        "gcn.classic.voevent.SWIFT_FOM_OBS",
        # "gcn.classic.voevent.SWIFT_FOM_PPT_ARG_ERR",
        # "gcn.classic.voevent.SWIFT_FOM_SAFE_POINT",
        # "gcn.classic.voevent.SWIFT_FOM_SLEW_ABORT",
        "gcn.classic.voevent.SWIFT_POINTDIR",
        "gcn.classic.voevent.SWIFT_SC_SLEW",
        "gcn.classic.voevent.SWIFT_TOO_FOM",
        "gcn.classic.voevent.SWIFT_TOO_SC_SLEW",
        "gcn.classic.voevent.SWIFT_UVOT_DBURST",
        "gcn.classic.voevent.SWIFT_UVOT_DBURST_PROC",
        "gcn.classic.voevent.SWIFT_UVOT_EMERGENCY",
        "gcn.classic.voevent.SWIFT_UVOT_FCHART",
        "gcn.classic.voevent.SWIFT_UVOT_FCHART_PROC",
        "gcn.classic.voevent.SWIFT_UVOT_POS",
        "gcn.classic.voevent.SWIFT_UVOT_POS_NACK",
        "gcn.classic.voevent.SWIFT_XRT_CENTROID",
        # "gcn.classic.voevent.SWIFT_XRT_EMERGENCY",
        "gcn.classic.voevent.SWIFT_XRT_IMAGE",
        "gcn.classic.voevent.SWIFT_XRT_IMAGE_PROC",
        "gcn.classic.voevent.SWIFT_XRT_LC",
        "gcn.classic.voevent.SWIFT_XRT_POSITION",
        "gcn.classic.voevent.SWIFT_XRT_SPECTRUM",
        "gcn.classic.voevent.SWIFT_XRT_SPECTRUM_PROC",
        "gcn.classic.voevent.SWIFT_XRT_SPER",
        "gcn.classic.voevent.SWIFT_XRT_SPER_PROC",
        "gcn.classic.voevent.SWIFT_XRT_THRESHPIX",
        "gcn.classic.voevent.SWIFT_XRT_THRESHPIX_PROC",
        # "gcn.classic.voevent.AAVSO",
        # "gcn.classic.voevent.ALEXIS_SRC",
        # "gcn.classic.voevent.BRAD_COORDS",
        # "gcn.classic.voevent.CBAT",
        "gcn.classic.voevent.COINCIDENCE",
        # "gcn.classic.voevent.COMPTEL_SRC",
        # "gcn.classic.voevent.DOW_TOD",
        "gcn.classic.voevent.GRB_CNTRPART",
        # "gcn.classic.voevent.GRB_COORDS",
        # "gcn.classic.voevent.GRB_FINAL",
        # "gcn.classic.voevent.GWHEN_COINC",
        "gcn.classic.voevent.HAWC_BURST_MONITOR",
        # "gcn.classic.voevent.HUNTS_SRC",
        "gcn.classic.voevent.KONUS_LC",
        # "gcn.classic.voevent.MAXBC",
        # "gcn.classic.voevent.MILAGRO_POS",
        # "gcn.classic.voevent.MOA",
        # "gcn.classic.voevent.OGLE",
        # "gcn.classic.voevent.SIMBADNED",
        "gcn.classic.voevent.SK_SN",
        "gcn.classic.voevent.SNEWS",
        # "gcn.classic.voevent.SUZAKU_LC",
        "gcn.classic.voevent.TEST_COORDS",
        "gcn.circulars",
        # "gcn.heartbeat",
        "gcn.notices.icecube.lvk_nu_track_search",
        "igwn.gwalert",
        "gcn.notices.swift.bat.guano",
        "gcn.notices.einstein_probe.wxt.alert",
    ]
)
messageid = 0
while True:
    for message in consumer.consume(timeout=1):
        if message.error():
            print(message.error())
            continue
        value = message.value()
        topic = message.topic()

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        fname = f"output/{now}_{messageid}_{topic}.xml"
        with open(fname, "w") as f:
            if isinstance(value, bytes):
                f.write(value.decode("utf-8"))
            else:
                f.write(value)
            messageid += 1
            print(f"Saved message from {topic} to {fname}")
