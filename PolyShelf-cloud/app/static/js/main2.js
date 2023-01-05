
var open_file = function(file) {
    return function() {
	window.open("/getfile/" + file);
    };
}

var change_folder = function(folder) {
    return function() {
    window.location.replace("/drive")
	cd(folder);
    };
};

var fill_in_files = function(data, id) {
    list = document.getElementById(id);
    list.innerHTML = "";
    if(data.length == 0)
	list.innerHTML = "";
    for(var i=0; i<data.length; ++i) {
	li = document.createElement('li');
	img = document.createElement('img');
	img.src = '/static/img/file.png';
	img.style.width = '50px';
	li.appendChild(img);
	li.appendChild(document.createTextNode(data[i]));
	list.appendChild(li);
	li.onclick = open_file(data[i])
    }
};

var fill_in_sizes = function(data, id) {
    list = document.getElementById(id);
    list.innerHTML = "";
    for(var i=0; i<data.length; ++i) {
	li = document.createElement('li');
	li.appendChild(document.createTextNode(data[i]));
	list.appendChild(li);
    }
};

var fill_in_folders = function(data, id) {
    list = document.getElementById(id);
    list.innerHTML = "";
    if(data.length == 0)
	list.innerHTML = "";
    for(var i=0; i<data.length; ++i) {
	li = document.createElement('li');
	img = document.createElement('img');
	img.src = '/static/img//folder.png';
	img.style.width = '50px';
	li.appendChild(img);
	li.appendChild(document.createTextNode(data[i]));
	list.appendChild(li);
	li.onclick = change_folder(data[i]);
    }
};

var ls = function() {
    var xhr = new XMLHttpRequest();
    var url = "/getFiles";
    xhr.open("GET", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
//            console.log(json);
	    console.log(json.files);
	    console.log(json.folders);
	    fill_in_files(JSON.parse(json.files), "files");
	    fill_in_folders(JSON.parse(json.folders), "folders");
	    fill_in_sizes(JSON.parse(json.file_size), "file_sizes");
	}
    };
    xhr.send();
};

var cd = function(folder) {
    var xhr = new XMLHttpRequest();
    var url = "/changedir";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
	    document.getElementById('current').innerHTML = "Current Directory: " +  json.direc;
	    ls();
	}
    };
    var data = JSON.stringify({"change_dir":folder});
    xhr.send(data);
};

ls();

var delete_file = function(file) {
    var xhr = new XMLHttpRequest();
    var url = "/delete";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
	    
	    ls();
	}
    };
    var data = JSON.stringify({"del_file":file});
    xhr.send(data);
};

buttons = ['alt0', 'alt1', 'alt2']
divs = ['section1', 'section2', 'section3']
names = ['Add File', 'Create New Folder', 'Delete File/Folder']

var toggle = function(id1, id2, name) {
    return function() {
	for(var i=0; i<3; ++i) {
	    document.getElementById(divs[i]).style.display='none';
	}
	document.getElementById(id2).style.display='block';
    };
}

buttons = ['alt0', 'alt1', 'alt2']
divs = ['section1', 'section2', 'section3']
names = ['Add File', 'Create New Folder', 'Delete File/Folder']

for(var i=0; i<3; ++i) {
    document.getElementById(buttons[i]).onclick = toggle(buttons[i], divs[i], names[i]);
    document.getElementById(buttons[i]).innerHTML = names[i];
    document.getElementById(divs[i]).style.display = 'none';
}
    document.getElementById(divs[0]).style.display = 'block';

var submitfunction = function() {
    file = document.getElementById('del_file_name').value;
    console.log(file);
    var xhr = new XMLHttpRequest();
    var url = "/delete";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
	    ls();
	}
    };
    var data = JSON.stringify({'del_file':file})
    xhr.send(data);
}

document.getElementById('delbutton').onclick=submitfunction

cd(".");
