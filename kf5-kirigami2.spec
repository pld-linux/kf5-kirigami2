#
# TODO:
# - runtime Requires if any

%define		kdeframever	5.39
%define		qtver		5.8.0
%define		kfname		kirigami2
Summary:	Kirigami2 library
Name:		kf5-%{kfname}
Version:	5.39.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	98c1dfd5fce54eac7071fb040affb461
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	catdoc
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kirigami2 library.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang libkirigami2plugin --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libkirigami2plugin.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5Kirigami2.so.5
%{_libdir}/libKF5Kirigami2.so.5.*.*
%{_libdir}/qt5/qml/org/kde/kirigami.2


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Kirigami2
%{_libdir}/cmake/KF5Kirigami2
%{_libdir}/libKF5Kirigami2.so
%{_libdir}/qt5/mkspecs/modules/qt_Kirigami2.pri
