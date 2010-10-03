%define		plugin		graphviz
Summary:	DokuWiki Graph Visualization Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20100821
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://github.com/splitbrain/dokuwiki-plugin-%{plugin}/zipball/master#/%{plugin}.zip
# Source0-md5:	54f864d57574daef265c36840b3fffca
Patch0:		mediainclude.patch
URL:		http://www.dokuwiki.org/plugin:graphviz
BuildRequires:	rpmbuild(macros) >= 1.520
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
%patch0 -p1

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,VERSION}

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.txt
%{plugindir}/*.php
%{plugindir}/*.png
%{plugindir}/conf
