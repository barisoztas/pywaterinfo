.. _groupids:

===================
Timeseriesgroup_ids
===================

Introduction
------------

For a number of time series, the VMM and HIC provide the group identifiers in the online
`available documentation <https://www.waterinfo.be/download/c4bc2c28-0251-40e3-8ecb-a139298597aa>`_.
These identifiers are the preferred source to query the enlisted variables.

.. note:: When you only require yearly aggregations, check for a time series with a corresponding
   frequency to overcome large data queries as much as possible.


VMM
---

For the VMM, the list of available group identifiers (date: 2017-10-01) are provided in the following table.

.. Caution:: These identifiers are not described as stable identifiers and can change in time!

.. csv-table:: VMM published timeseriesgroup identifiers
   :header: "variable (nl)", "frequency_nl", "timeseriesgroup_id", "variable (en)", "frequency (en)"

      afvoer, 15min, 192786, discharge, 15min
      afvoer, uur, 192892, discharge, hour
      afvoer, dag, 192893, discharge, day
      afvoer, maand, 192894, discharge, month
      afvoer, jaar, 192895, discharge, year
      bodem_verzadiging, 15min, 192929, soil_saturation, 15min
      bodem_vocht, 15min, 192928, soil_moisture, 15min
      dauwpunt_temperatuur, 15min, 192923, dew_point_temperature, 15min
      geleidbaarheid (permanent meetnet), 15min, 383065, conductivity (continuous network), 15min
      geleidbaarheid (project), 15min, 381863, conductivity (project based), 15min
      grondtemperatuur, 15min, 192924, ground_temperature, 15min
      grondwarmte, 15min, 192916, ground_heat, 15min
      instraling, 15min, 192920, irradiance, 15min
      luchtdruk, 15min, 192918, air_pressure, 15min
      luchttemperatuur175cm, 15min, 192922, air_temperature_175cm, 15min
      neerslag, 1m, 199792, rainfall, 1min
      neerslag, 15min, 192896, rainfall, 15min
      neerslag, uur, 192897, rainfall, hour
      neerslag, dag, 192898, rainfall, day
      neerslag, maand, 192899, rainfall, month
      neerslag, jaar, 192900, rainfall, year
      relatieve_vochtigheid, 15min, 192919, relative_humidity, 15min
      verdamping_monteith, 15min, 192927, evaporation_monteith, 15min
      verdamping_monteith, dag, 295480, evaporation_monteith, day
      verdamping_monteith, maand, 295482, evaporation_monteith, month
      verdamping_monteith, jaar, 295483, evaporation_monteith, year
      verdamping_penman, 15min, 204341, evaporation_penman, 15min
      verdamping_penman, dag, 295474, evaporation_penman, day
      verdamping_penman, maand, 295475, evaporation_penman, month
      verdamping_penman, jaar, 295479, evaporation_penman, year
      watersnelheid, 15min, 192901, water_velocity, 15min
      watersnelheid, uur, 192902, water_velocity, hour
      watersnelheid, dag, 192903, water_velocity, day
      watersnelheid, maand, 192904, water_velocity, month
      watersnelheid, jaar, 192905, water_velocity, year
      waterstand, 15min, 192780, water_level, 15min
      waterstand, uur, 192785, water_level, hour
      waterstand, dag, 192782, water_level, day
      waterstand, maand, 192783, water_level, month
      waterstand, jaar, 192784, water_level, year
      watertemperatuur, 15min, 325066, water_temperature, 15min
      windrichting, 15min, 192926, wind_direction, 15min
      windspeed, 15min, 192925, wind_speed, 15min

HIC - Cmd timeseriesgroup_ids
-----------------------------

The list of available group identifiers for Cmd (Continuously
Measured) time series (date: 2025-09-06) are provided in the following table.

.. Caution:: These identifiers are not described as stable identifiers and can change in time!

.. csv-table:: HIC - Cmd timeseriesgroup_ids
   :header: "group_id", "group_name", "group_type", "stationparameter_longname", "ts_unitname", "ts_unitsymbol"
   :widths: 10, 15, 15, 10, 10, 5

      156149,WEB_L_Discharge_All,timeseries,River Discharge,cubic meter per second,m³/s
      156152,WEB_L_Status_All,timeseries,River Stage,Alarmstatus,Alarmstatus
      156153,WEB_L_StatusKT_All,timeseries,H_voorspeld,Alarmstatus,Alarmstatus
      156154,WEB_L_Waterlevel_All,timeseries,River Stage,meter,m
      156155,WEB_TS_DrempelPrewaak_ALL,timeseries,River Stage,meter,m
      156156,WEB_TS_DrempelWaak_ALL,timeseries,River Stage,meter,m
      156157,WEB_TS_DrempelAlarm_ALL,timeseries,River Stage,meter,m
      156161,DEX_YAMItoolreeksen,timeseries,W_voorspeld,meter,m
      156163,DL_H_hr,timeseries,River Stage,meter,m
      156165,DL_HWLW,timeseries,Tidal Water Level,meter,m
      156170,DL_Q_hr,timeseries,River Discharge,cubic meter per second,m³/s
      156172,DL_Chlorofyl,timeseries,Chlorofyl a,microgram per litre,µg/l
      156173,DL_Conductiviteit,timeseries,Conductivity,microsiemens per centimeter,µS/cm
      156179,WEB_L_Waterlevel_zonder_status,timeseries,River Stage,meter,m
      156180,WEB_L_Status_Scheld,timeseries,Tidal Water Level,Alarmstatus,Alarmstatus
      156181,WEB_L_StatusKT_Scheld,timeseries,W_voorspeld,Alarmstatus,Alarmstatus
      156183,WEB_L_WaterlevelTij_Scheld_meting_zonder_status_metvoorspelling,timeseries,Tidal Water Level,meter,m
      156188,DL_SSC,timeseries,Suspended Sediment Concentration Calculated,milligram per litre,mg/l
      156192,DEX_RWS_HMC,timeseries,River Discharge,cubic meter per second,m³/s
      156196,WEB_L_WaterlevelTij_meting_zonder_status_metofzonder_voorspelling,timeseries,River Stage,meter,m
      156197,DL_pH,timeseries,pH,scalar,-
      156198,WEB_L_Status_HIC,timeseries,River Stage,Alarmstatus,Alarmstatus
      156199,DL_Snelheid_Sediment,timeseries,Flow Velocity,meter per second,m/s
      156200,DL_Temperatuur_Sediment,timeseries,Temperature,degree Celsius,°C
      156202,DL_Turbiditeit,timeseries,Turbidity_NTU,nephlometric turbidity unit,NTU
      156203,WEB_L_StatusLT_Scheld,timeseries,W_voorspeld,Alarmstatus,Alarmstatus
      156204,WEB_L_Waterlevel_HICwithoutstatus,timeseries,River Stage,meter,m
      156206,WEB_L_Windsnelheid,timeseries,Wind Speed,meter per second,m/s
      156207,DL_Zuurstofgehalte,timeseries,Oxygen Concentration,milligram per litre,mg/l
      156208,DL_Zuurstofverzadiging,timeseries,Oxygen Saturation,percentage,%
      245283,WEB_L_Discharge_Scheld,timeseries,River Discharge,cubic meter per second,m³/s
      245286,WEB_L_Teststations,timeseries,River Discharge,cubic meter per second,m³/s
      246424,DEX_Visuris,timeseries,River Stage,meter,m
      253643,DEX_Vito_DCS4COP,timeseries,Tidal Water Level,meter,m
      256286,M_HIC_Spanning12V,timeseries,Battery Voltage,volt,V
      271671,DEX_Bruxelles_Environnement,timeseries,River Stage,meter,m
      274268,DEX_DVW_Maasafvoer,timeseries,River Discharge,cubic meter per second,m³/s
      350099,DL_astroHWLW_TAW,timeseries,W_voorspeld,meter,m
      368706,DEX_LIFE_Sparc,timeseries,W_voorspeld,meter,m
      416414,WEB_L_StatusLT_All,timeseries,H_voorspeld,Alarmstatus,Alarmstatus
      420471,ZZ_WVE_W_HW,timeseries,Tidal Water Level,meter,m
      420473,ZZ_WVE_W_LW,timeseries,Tidal Water Level,meter,m
      421208,DL_Saliniteit,timeseries,Salinity,Practical salinity scale,psu
      433534,DEX_VMM_operationeel-metingen,timeseries,River Stage,meter,m
      442133,DEX_EFAS,timeseries,River Stage,meter,m
      461382,WEB_L_Chlorofyl,timeseries,Chlorofyl a,microgram per litre,µg/l
      461383,WEB_L_Conductiviteit,timeseries,Conductivity,microsiemens per centimeter,µS/cm
      461384,WEB_L_pH,timeseries,pH,scalar,-
      461385,WEB_L_Saliniteit,timeseries,Salinity,Practical salinity scale,psu
      461387,WEB_L_Snelheid_Sediment,timeseries,Flow Velocity,meter per second,m/s
      461389,WEB_L_Temperatuur_Sediment,timeseries,Temperature,degree Celsius,°C
      461390,WEB_L_Turbiditeit,timeseries,Turbidity_NTU,nephlometric turbidity unit,NTU
      461391,WEB_L_Zuurstofgehalte,timeseries,Oxygen Concentration,milligram per litre,mg/l
      461392,WEB_L_Zuurstofverzadiging,timeseries,Oxygen Saturation,percentage,%
      461393,WEB_L_SSC,timeseries,Suspended Sediment Concentration Calculated,milligram per litre,mg/l
      490757,ZZ_WVE_SAL_MONEOS,timeseries,Salinity,Practical salinity scale,psu
      491410,ZZ_WVE_T_MONEOS,timeseries,Temperature,degree Celsius,°C
      491732,WEB_L_GaugingsDiff,timeseries,River Stage,meter,m
      492671,ZZ_WVE_V_MONEOS,timeseries,Flow Velocity,meter per second,m/s
      492711,ZZ_LBX_KT1D perc,timeseries,W_voorspeld,meter,m
      493297,ZZ_JBS_H_Q_DES,timeseries,River Stage,meter,m
      495222,DEX_ABBA,timeseries,River Stage,meter,m
      495828,ZZ_WVE_SSC_calc_MONEOS,timeseries,Suspended Sediment Concentration Calculated,milligram per litre,mg/l
      505696,ZZ_WVE_WT_All,timeseries,Temperature,degree Celsius,°C
      507289,ZZ_LBX_meetperiodePiekenExtended,timeseries,River Discharge,cubic meter per second,m³/s
      510205,DL_HW,timeseries,Tidal Water Level,meter,m
      510207,DL_LW,timeseries,Tidal Water Level,meter,m
      512458,DL_astroContinu_LAT,timeseries,W_voorspeld,decimeter,dm
      513106,DEX_SMS_Status,timeseries,River Stage,Alarmstatus,Alarmstatus
      513111,DEX_SMS_Prewaak_MeldingBoven1,timeseries,Tidal Water Level,meter,m
      513112,DEX_SMS_Waak_MeldingBoven2,timeseries,River Stage,meter,m
      513113,DEX_SMS_Alarm_MeldingBoven3,timeseries,River Stage,meter,m
      514487,DEX_COTU,timeseries,Tidal Water Level,meter,m
      515316,DL_astroHWLW_LAT,timeseries,W_voorspeld,decimeter,dm
      515326,ZZ_PVE_HWLW-metingen_YAMI,timeseries,Tidal Water Level,meter,m
      526977,DEX_VNF,timeseries,River Stage,meter,m
      528877,DEX_RWS_DCM,timeseries,River Stage,meter,m
      2987910,WEB_TS_DrempelAlarm_SIGN,timeseries,River Stage,meter,m
      2987911,WEB_TS_DrempelWaak_SIGN,timeseries,River Stage,meter,m
      2987912,WEB_TS_DrempelPrewaak_SIGN,timeseries,Tidal Water Level,meter,m
      3055290,DEX_Meet-het,timeseries,Tidal Water Level,meter,m
      3140709,DEX_Astrotool-WL,timeseries,W_voorspeld,meter,m
      3160809,DEX_WL_EO,timeseries,Temperature,degree Celsius,°C
      3168990,DEX_Meet-het3,timeseries,Tidal Water Level,meter,m
      3295428,DEX_SMS_StatusLT,timeseries,W_voorspeld,Alarmstatus,Alarmstatus



HIC - Ensemble timeseriesgroup_ids
----------------------------------

The list of available group identifiers for ensemble time series (date: 2025-09-06) are
provided in the following table.

.. Caution:: These identifiers are not described as stable identifiers and can change in time!


.. csv-table:: HIC - Cmd timeseriesgroup_ids
   :header: "group_id", "group_name", "group_type", "stationparameter_longname", "ts_unitname", "ts_unitsymbol"
   :widths: 10, 15, 15, 10, 10, 5

      156151,WEB_L_PluvioKT,timeseries,Ncatch_voorspeld,millimeter,mm
      245288,WEB_L_WaterlevelKT_voorspellingspunten,timeseries,Q_voorspeld,cubic meter per second,m³/s
      385328,DEX_BOS_KGT,timeseries,Q_voorspeld,cubic meter per second,m³/s
      432821,DL_VerwachtingenHWLW,timeseries,W_voorspeld,meter,m
      473642,DEX_VMM_operationeel-voorspellingen,timeseries,H_voorspeld,meter,m
      506056,DL_PeilVoorspeld_KTdet,timeseries,H_voorspeld,meter,m
      506057,DL_AfvoerVoorspeld_KTdet,timeseries,Q_voorspeld,cubic meter per second,m³/s
      506058,DL_PeilVoorspeld_LTdet,timeseries,H_voorspeld,meter,m
      506059,DL_AfvoerVoorspeld_LTdet,timeseries,Q_voorspeld,cubic meter per second,m³/s
      506060,DL_NCatch_KTdet,timeseries,Ncatch_voorspeld,millimeter,mm
      506061,DL_NCatch_LTdet,timeseries,Ncatch_voorspeld,millimeter,mm
      507290,ZZ_LBX_NCatchvoorspeld,timeseries,Ncatch_voorspeld,millimeter,mm
      514458,ZZ_PVE_@test-externe-vsn,timeseries,H_voorspeld,meter,m
      515366,ZZ_PVE_VSSKS_UNLPUTV,timeseries,Q_voorspeld,cubic meter per second,m³/s
      2937448,DEX_MDK_OMS,timeseries,W_voorspeld,meter,m
      3136706,V_RWS-DREAL-SPW_H-Q,timeseries,Q_voorspeld,cubic meter per second,m³/s
      3138273,ZZ_LBX_KT,timeseries,H_voorspeld,meter,m
