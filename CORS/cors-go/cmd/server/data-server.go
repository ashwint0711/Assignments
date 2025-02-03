package main

import (
	"fmt"
	"net/http"
)

func pingRequestHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodGet {
		//Writing response to a file (i.e to a socket)
		fmt.Fprint(w, "Pong\n")
	} else {
		http.Error(w, "Unsupported method\n", http.StatusMethodNotAllowed)
	}
}

func dataRequestHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "http://localhost:9000")
	w.Header().Set("Access-Control-Allow-Methods", "OPTIONS, GET")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	if r.Method == http.MethodGet {
		w.WriteHeader(http.StatusOK)
		fmt.Fprint(w, "Response to a GET request")
	}
}

func main() {
	http.HandleFunc("/ping", pingRequestHandler)
	http.HandleFunc("/api/data", dataRequestHandler)
	fmt.Println("Starting server on port 9500")
	err := http.ListenAndServe(":9500", nil)
	if err != nil {
		fmt.Println("Failed to start server!!")
	}
}
