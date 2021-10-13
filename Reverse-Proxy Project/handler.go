package main

import {
	"net/http"
	"net/http/httputil"
	"net/url"
	"os"
	"strings"
}

func init()  {
	http.DefaultTransport.(*http.Transport).TLSClientConfig
}