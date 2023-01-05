var cd = function(folder) {
    var xhr = new XMLHttpRequest();
    var url = "/changedir";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
	}
    };
    var data = JSON.stringify({"change_dir":folder});
    xhr.send(data);
};

var ls = function() {
    var xhr = new XMLHttpRequest();
    var url = "/changedir";
    xhr.open("GET", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
	}
    };
};

