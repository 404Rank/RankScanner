'use strict';

function urlFormat(url) {
    var AURL = document.createElement("a"),
        UFormat = {};
    AURL.href = url;
    UFormat.protocal = AURL.protocol;
    UFormat.hostname = AURL.hostname;
    UFormat.port = AURL.port;
    UFormat.path = AURL.path;
    UFormat.pathname = AURL.pathname;
    UFormat.query = AURL.query;
    return UFormat || {
        protocal: "",
        hostname: "",
        port: "",
        path: "",
        pathname: "",
        query: ""
    };
}