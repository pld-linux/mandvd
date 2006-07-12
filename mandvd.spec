Summary:	ManDVD
Summary(pl):	ManDVD
Name:		mandvd
Version:	2.0.5
Release:	0.3
License:	GPL
Group:		X11/Application
Source0:	http://csgib36.ifrance.com/FTP/%{name}-%{version}src.tar.gz
# Source0-md5:	f2d835361e241df348d6eb337bc8bf9b
Source1:	%{name}.desktop
URL:		http://www.kde-apps.org/content/show.php?content=38347
BuildRequires:	qt-devel >= 6:3.3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl
 
%prep
%setup -q -n ManDVD-%{version}

%build
export QTDIR=%{_prefix}
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_iconsdir}/hicolor/128x128/apps,%{_desktopdir}}
install mandvd $RPM_BUILD_ROOT%{_bindir}/mandvd
install mandvdico.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps/mandvdico.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mandvd
%{_iconsdir}/hicolor/*/apps/mandvdico.png
%{_desktopdir}/%{name}.desktop
