package context

import (
	"encoding/json"
	"io"
	"io/ioutil"
	"log"
	"os"
	"path"
)

type ConfigOperation interface {
	Get(key string) (string, bool)
	Set(key string, value string)
}

type ConfigStore struct {
	path  string
	items map[string]string
}

func NewConfigOperation() ConfigOperation {
	localConfigStorePath := path.Join(os.Getenv("HOME"), ".butler/config")
	store := &ConfigStore{
		path:  localConfigStorePath,
		items: make(map[string]string),
	}

	store.readAll()

	return store
}

func (store *ConfigStore) Get(key string) (string, bool) {
	configItem, existed := store.items[key]
	return configItem, existed
}

func (store *ConfigStore) Set(key string, value string) {
	store.items[key] = value
	store.write()
}

func (store *ConfigStore) readAll() {
	file, err := os.Open(store.path)
	if err != nil {
		if os.IsNotExist(err) {
			return
		}

		log.Fatal("open config error", err)
	}

	defer closeResource(file)

	err = json.NewDecoder(file).Decode(&store.items)
	if err != nil {
		log.Fatal("config decode fail", err)
	}
}

func (store *ConfigStore) write() {
	content, err := json.MarshalIndent(store.items, "", "")
	if err != nil {
		log.Fatal("json marsha fail", err)
	}

	err = ioutil.WriteFile(store.path, content, 0644)
	if err != nil {
		log.Fatal("write marsha fail", err)
	}
}

func closeResource(closer io.Closer) {
	err := closer.Close()
	if err != nil {
		log.Fatal("close resource fail", err)
	}
}
