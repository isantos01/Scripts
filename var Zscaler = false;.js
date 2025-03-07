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

//////
var QuotaExceededError = false;
var parsed = JSON.parse(VTresponse);

if (parsed.error && parsed.error.code == "NotFoundError") {
    QuotaExceededError;
} else if (parsed.error && parsed.error.code == "QuotaExceededError") {
    QuotaExceededError = true;
}
QuotaExceededError == false;

var Error = JSON.parse(VTresponse).error.code;
Error == "NotFoundError";

/////////
,
{
    "stellarHost": "https://soc2.digicelbusinessprotect.com",
        "stellarAuthKey": "c3VwcG9ydEBoeXBlcmNlbnRyYWwuY28udWs6U0tKVmRXR3FXMkxMQy1uVElTR3F2eHppNXZBbjRDTmZQalVBNmZHcHcyd0hTQ3NuWEZRVE5xZ3JWZlR0N3VQNGJXUTNlTXFKV2s1ODVPRmlMaGFuTXc="
}
////////
var Zscaler = false;
var alerts = JSON.parse(alerts);

for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i]; // This is an array per JSON

    if ("msg_data" in alert._source) {
        const string = JSON.stringify(alert._source.msg_data);
        if (string.indexOf("Zscaler") > -1 || alert.dstip_host && alert.dstip_host.indexOf("zpath") > -1) {
            Zscaler = true;
        }
    }
}
Zscaler;
/////////////
var res = JSON.parse(VTresponse);
var Error;

if (res.error && res.error.code) {
    Error = res.error.code;
}
Error !== "NotFoundError"
///////////
var processResults = JSON.parse(processResults);
var dedup = false;

var spin = S(response);
var res = JSON.parse(spin);
var array;

if (res.data && res.data.totalReports) {
    var totalReports = res.data.totalReports;
    array = abuseIpReportCount;
    array.add(totalReports);
} else {
    var TotalReports = 0;
    array = abuseIpReportCount;
    array.add(TotalReports);
}
array;
////////////
var parsed = JSON.parse(alert)
var dstip;

if (parsed._source && parsed._source.dstip) {
    dstip = parsed._source.dstip;
} else {
    dstip = "0.0.0.0";
}
dstip;
//////////
var parsed = JSON.parse(alert);
var srcip;
if (parsed._source && parsed._source.srcip) {
    srcip = parsed._source.srcip;
} else if (parsed._source && parsed._source.hostip) {
    srcip = parsed._source.hostip;
}
srcip;

///////////////
var res = JSON.parse(VTresponse);
var Error;

if (res.error && res.error.code) {
    Error = res.error.code;
}
Error == "NotFoundError"
/////////////////
var IsMalicious = false;
var VTresponse = VTdomainCount;
var URLresponse = UrlAnalysis;

for (var i = 0; i < VTresponse.length || i < URLresponse.length; i++) {
    const VTelement = VTresponse[i];
    const URLelement = URLresponse[i];
    if (VTelement >= 3 || URLelement >= 4) {
        IsMalicious = true;
    }
}
IsMalicious == true;
//////////////////////
var IsMalicious = false;
var VTresponse = VTdomainCount;
var URLresponse = UrlAnalysis;

if (VTresponse.length == 0) {
    for (var i = 0; i < URLresponse.length; i++) {
        const URLelement = URLresponse[i];
        if (URLelement >= 4) {
            IsMalicious = true;
            break;
        }
    }
} else if (URLresponse.length == 0) {
    for (var i = 0; i < VTresponse.length; i++) {
        const VTelement = VTresponse[i];
        if (VTelement >= 3) {
            IsMalicious = true;
            break;
        }
    }
}
IsMalicious == true;
///////////// addition
else {
    for (var i = 0; i < Math.max(VTresponse.length || URLresponse.length); i++) {
        const VTelement = VTresponse[i];
        const URLelement = URLresponse[i];
        if (i < VTresponse.length && VTelement >= 3 || i < URLelement.length && URLelement >= 4) {
            IsMalicious = true;
        }
    }
}
////////////
var IsMalicious = false;
var response = UrlAnalysis;

for (i = 0; i < response.length; i++) {
    const element = response[i];
    if (element >= 4) {
        IsMalicious = true;
    }
}
IsMalicious;
//////////
var IsMalicious = false;
var response = VTdomainCount;

for (i = 0; i < response.length; i++) {
    const element = response[i];
    if (element >= 3) {
        IsMalicious = true;
    }
}
IsMalicious;
////////
var domain;
var Data = JSON.parse(alert);

if (Data._source && Data._source.domain_list && Data._source.domain_list.length > 0) {
    domain = Data._source.domain_list[0];
} else if (Data._source.metadata && Data._source.metadata.request && Data._source.metadata.request.query) {
    domain = Data._source.metadata.request.query;
}
domain;
///////////////////////
var domain;
var Data = JSON.parse(alert);

if (Data._source && Data._source.metadata && Data._source.metadata.request && Data._source.metadata.request.query) {
    domain = Data._source.metadata.request.query;
} else if (Data._source && Data._source.domain_list && Data._source.domain_list.length > 0) {
    var string = JSON.stringify(alert._source.domain_list)
    domain = string.replace(/^\["|"\]$/g, "");
}
domain;
////////
var domain;
var Data = JSON.parse(alert);

if (Data._source && Data._source.metadata && Data._source.metadata.request && Data._source.metadata.request.query) {
    domain = Data._source.metadata.request.query;
} else if (Data._source && Data._source.metadata && Data._source.metadata.response && Data._source.metadata.response.query) {
    domain = Data._source.metadata.response.query;
} else if (Data._source && Data._source.domain_list && Data._source.domain_list.length > 0) {
    domain = Data._source.domain_list[0];
}
domain;
//////////
var array = JSON.parse(processResults);

let index = array.findIndex(item => item.caseId === caseId);
if (index !== -1) {
    array.splice(index, 1);
}

array.push({
    "environment": stellarHost,
    "caseId": caseId,
    "result": "False Positive",
    "allIpsPrivate": allIpsPrivate,
    "firewallAction": firewallAction,
    "scoreOver70": scoreOver70,
    "seriousThreatName": seriousThreatName
});

processResults = JSON.stringify(array);
////////////////////
var array = JSON.parse(processResults);
array.push({ "environment": stellarHost, "caseId": caseId, "result": "False Positive", "allIpsPrivate": allIpsPrivate, "firewallAction": firewallAction, "scoreUnder10": scoreUnder10, "seriousThreatName": seriousThreatName });
JSON.stringify(array);
//////////////////////
var array = JSON.parse(processResults);
array.push({ "environment": stellarHost, "caseId": caseId, "result": "Real Threat", "allIpsPrivate": allIpsPrivate, "firewallAction": firewallAction, "scoreOver70": scoreOver70, "seriousThreatName": seriousThreatName });
JSON.stringify(array);