var Zscaler = false;
var alerts = JSON.parse(alerts);

for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i]; // This is an array per JSON

    if ("msg_data" in alert._source) {
        var string = JSON.stringify(alert.msg_data);
        if (string.indexOf("Zscaler") > -1) {
            Zscaler = true;
        }
    }
}
Zscaler;

/////////////////
var Zscaler = false;
var alerts = JSON.parse(alerts);
var response;
var FoundZscaler;

for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i]; // This is an array per JSON

    if ("msg_data" in alert._source) {
        response = JSON.stringify(alert._source.msg_data);
        FoundZscaler = response.indexOf("Zscaler");
        if (FoundZscaler > -1) {
            Zscaler = true;
        }
    }
}
Zscaler;
///////////
var Zscaler = false;
var alerts = JSON.parse(alerts);

for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i]; // This is an array per JSON

    if ("msg_data" in alert._source) {
        const string = JSON.stringify(alert._source.msg_data);
        if (string.indexOf("Zscaler") > -1 || alert.dstip_host.indexOf("zpath") > -1) {
            Zscaler = true;
        }
    }
}
Zscaler;
////////////////

var isp = JSON.parse(DstResponse).isp;
var array;

if (isp == "Akamai Technologies, Inc.") {
    const TotalReports = 0;
    array = abuseIpReportCount;
    array.add(TotalReports);
} else {
    const TotalReports = JSON.parse(DstResponse).totalReports;
    array = abuseIpReportCount;
    array.add(TotalReports);
}
array;

////////////
var isp = JSON.parse(SrcResponse).isp;
var array;

if (isp == "Akamai Technologies, Inc.") {
    const TotalReports = 0;
    array = abuseIpReportCount;
    array.add(TotalReports);
} else {
    const TotalReports = JSON.parse(SrcResponse).totalReports;
    array = abuseIpReportCount;
    array.add(TotalReports);
}
array;


///
alerts = JSON.parse(alerts);
var allIpsPrivate = false;
var totalSrcIps = 0;
var totalDstIps = 0;
var privateSrcIps = 0;
var privateDstIps = 0;

for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i];
    if ('srcip_type' in alert._source) {
        var srcIpType = alert._source.srcip_type;
        totalSrcIps++;
        if (srcIpType == 'private') {
            privateSrcIps++;
        }
    }
    if ('dstip_type' in alert._source) {
        var dstIpType = alert._source.dstip_type;
        totalDstIps++;
        if (dstIpType == 'private') {
            privateDstIps++;
        }
    }
    if (i == alerts.length - 1) {
        if ((totalSrcIps == privateSrcIps) && (totalDstIps == privateDstIps) && (totalSrcIps !== 0 && totalDstIps !== 0)) {
            allIpsPrivate = true;
        }
    }
}

allIpsPrivate;

//