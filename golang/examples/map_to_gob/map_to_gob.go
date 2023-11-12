package main

import (
	"bufio"
	"bytes"
	_ "embed"
	"encoding/gob"
	"fmt"
	"os"
	"strconv"
	"strings"
)

//go:embed ZipLoc
var ZipGeoCoords []byte

type GeoCoord struct {
	LAT float64
	LGT float64
}

var ZipLoc map[string]GeoCoord

func writeFile(filename string, data []byte) {
	file, err := os.OpenFile(filename, os.O_CREATE|os.O_RDWR, 0777)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	_, err = file.Write(data)
	if err != nil {
		panic(err)
	}

}

func storeMapGob(filename string, data map[string]GeoCoord) {
	var buf bytes.Buffer
	enc := gob.NewEncoder(&buf)

	err := enc.Encode(data)
	if err != nil {
		panic(err)
	}

	writeFile(filename, buf.Bytes())
}

func readGob(data []byte) map[string]GeoCoord {
	out := make(map[string]GeoCoord)

	buf := bytes.NewBuffer(data)
	dec := gob.NewDecoder(buf)

	err := dec.Decode(&out)
	if err != nil {
		panic(err)
	}

	return out
}

func main() {

	m1 := readGob(ZipGeoCoords)
	fmt.Println(m1)

	fmt.Printf("\n\nZip: %s; Lat: %f; Lon: %f;\n\n", "28411", m1["28401"].LAT, m1["28411"].LGT)

	ZipLoc = make(map[string]GeoCoord)

	file, err := os.Open("./data/zip_centroid.csv")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	csvReader := bufio.NewReader(file)

	csvReader.ReadString('\n')
	s, err := csvReader.ReadString('\n')
	fmt.Println(s, err)

	for err == nil {
		tmp := strings.Split(s, ",")
		lat, _ := strconv.ParseFloat(strings.TrimSpace(tmp[1]), 64)
		lgt, _ := strconv.ParseFloat(strings.TrimSpace(tmp[2]), 64)
		ZipLoc[strings.TrimSpace(tmp[0])] = GeoCoord{lat, lgt}
		s, err = csvReader.ReadString('\n')
	}

	fmt.Println(s, err)
	storeMapGob("ZipLoc", ZipLoc)
}
