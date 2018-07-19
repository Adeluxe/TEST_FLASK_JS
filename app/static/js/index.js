(function() {

	function init() {
		$(load-btn).addEventListener('click', loaddata);
	}

	init();

	function loaddata() {
		var req = JSON.stringify({});
		ajax('GET', '/loaddata', req, function(res) {
			var svc = JSON.parse(res);
			listService(svc);
		},
		function() {
			alert('Service failed!');
		});
	}

	function listService(svcs) {
		var svcList = $('svc_list');
		svcList.innerHTML = '';

		for (var i = 0; i < svcs.length; i++) {
			addService(svcList, svcs[i]);
		}
	}

	function addService(svcList, svc) {
		var li = $('li', {
			id : 'svc-' + svc.xaa_re,
			className : 'svc'
		});
		li.innerHTML = svc.xaa_nm;
		svcList.appendChild(li);

	}

	function $(tag, options) {
		if (!options) {
			return document.getElementById(tag);
		}

		var element = document.createElement(tag);

		for ( var option in options) {
			if (options.hasOwnProperty(option)) {
				element[option] = options[option];
			}
		}

		return element;
	}

	/**
	 * AJAX helper
	 * 
	 * @param method -
	 *            GET|POST|PUT|DELETE
	 * @param url -
	 *            API end point
	 * @param callback -
	 *            This the successful callback
	 * @param errorHandler -
	 *            This is the failed callback
	 */
	function ajax(method, url, data, callback, errorHandler) {
		var xhr = new XMLHttpRequest();

		xhr.open(method, url, true);

		xhr.onload = function() {
			switch (xhr.status) {
			case 200:
				callback(xhr.responseText);
				break;
			case 403:
				onSessionInvalid();
				break;
			case 401:
				errorHandler();
				break;
			}
		};

		xhr.onerror = function() {
			console.error("The request couldn't be completed.");
			errorHandler();
		};

		if (data === null) {
			xhr.send();
		} else {
			xhr.setRequestHeader("Content-Type",
					"application/json;charset=utf-8");
			xhr.send(data);
		}
	}

}
)();