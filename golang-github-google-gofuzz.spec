Name     : golang-github-google-gofuzz
Version  : fd52762d25a41827db7ef64c43756fd4b9f7e382
Release  : 1
URL      : https://github.com/google/gofuzz/archive/fd52762d25a41827db7ef64c43756fd4b9f7e382.tar.gz
Source0  : https://github.com/google/gofuzz/archive/fd52762d25a41827db7ef64c43756fd4b9f7e382.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go

%description
gofuzz
======
gofuzz is a library for populating go objects with random values.
[![GoDoc](https://godoc.org/github.com/google/gofuzz?status.png)](https://godoc.org/github.com/google/gofuzz)
[![Travis](https://travis-ci.org/google/gofuzz.svg?branch=master)](https://travis-ci.org/google/gofuzz)

%prep
%setup -q -n gofuzz-fd52762d25a41827db7ef64c43756fd4b9f7e382

%build
export LANG=C

%install
gopath="/usr/lib/golang"
library_path="github.com/google/gofuzz"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/google/gofuzz/doc.go
/usr/lib/golang/src/github.com/google/gofuzz/example_test.go
/usr/lib/golang/src/github.com/google/gofuzz/fuzz.go
/usr/lib/golang/src/github.com/google/gofuzz/fuzz_test.go
