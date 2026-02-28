%define		plugin		graphviz
Summary:	DokuWiki Graph Visualization Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20101124
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://github.com/splitbrain/dokuwiki-plugin-%{plugin}/zipball/master#/%{plugin}-%{version}.zip
# Source0-md5:	549b1025d6bcd8c6a317de8001327ae9
URL:		http://www.dokuwiki.org/plugin:graphviz
BuildRequires:	rpmbuild(macros) >= 1.520
BuildRequires:	unzip
Requires:	dokuwiki >= 20091225
Suggests:	graphviz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin can create directed and non-directed graph images from a
textual description language called “dot” using the Graphviz program.
It can use a locally installed graphviz or use Google's chart API for
rendering.

The plugin supports exporting to OpenOffice through the ODT Plugin
(only with a local graphviz install).

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/README

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/*.png
%{plugindir}/conf
