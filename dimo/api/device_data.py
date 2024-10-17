from typing import Optional


class DeviceData:

    def __init__(self, request_method, get_auth_headers):
        self._request = request_method
        self._get_auth_headers = get_auth_headers

    def get_vehicle_history(
        self,
        privileged_token: str,
        token_id: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        buckets: Optional[str] = None,
    ):
        params = {}
        if start_time is not None:
            params["startTime"] = start_time
        if end_time is not None:
            params["endTime"] = end_time
        if buckets is not None:
            params["buckets"] = buckets
        url = f"/v2/vehicle/{token_id}/history"
        return self._request(
            "GET",
            "DeviceData",
            url,
            params=params,
            headers=self._get_auth_headers(privileged_token),
        )

    def get_vehicle_status(self, privileged_token: str, token_id: str) -> dict:
        url = f"/v2/vehicle/{token_id}/status"
        return self._request(
            "GET", "DeviceData", url, headers=self._get_auth_headers(privileged_token)
        )

    def get_v1_vehicle_history(
        self,
        privileged_token: str,
        token_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        params = {}
        if start_date is not None:
            params["startDate"] = start_date
        if end_date is not None:
            params["endDate"] = end_date
        url = f"/v1/vehicle/{token_id}/history"
        return self._request(
            "GET",
            "DeviceData",
            url,
            params=params,
            headers=self._get_auth_headers(privileged_token),
        )

    def get_v1_vehicle_status(self, privileged_token: str, token_id: str) -> dict:
        url = f"/v1/vehicle/{token_id}/status"
        return self._request(
            "GET", "DeviceData", url, headers=self._get_auth_headers(privileged_token)
        )

    def get_v1_vehicle_status_raw(self, privileged_token: str, token_id: str) -> dict:
        url = f"/v1/vehicle/{token_id}/status-raw"
        return self._request(
            "GET", "DeviceData", url, headers=self._get_auth_headers(privileged_token)
        )

    def get_user_device_status(self, access_token: str, user_device_id: str) -> dict:
        url = f"/v1/user/device-data/{user_device_id}/status"
        return self._request(
            "GET", "DeviceData", url, headers=self._get_auth_headers(access_token)
        )

    def get_user_device_history(
        self,
        access_token: str,
        user_device_id: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> dict:
        params = {}
        if start_date is not None:
            params["startDate"] = start_date
        if end_date is not None:
            params["endDate"] = end_date
        url = f"/v1/user/device-data/{user_device_id}/historical"
        return self._request(
            "GET",
            "DeviceData",
            url,
            params=params,
            headers=self._get_auth_headers(access_token),
        )

    def get_daily_distance(
        self, access_token: str, user_device_id: str, time_zone: str
    ) -> dict:
        params = {"timeZone": time_zone}
        url = f"/v1/user/device-data/{user_device_id}/daily-distance"
        return self._request(
            "GET",
            "DeviceData",
            url,
            headers=self._get_auth_headers(access_token),
            params=params,
        )

    def get_total_distance(self, access_token: str, user_device_id: str) -> dict:
        url = f"/v1/user/device-data/{user_device_id}/distance-driven"
        return self._request(
            "GET", "DeviceData", url, headers=self._get_auth_headers(access_token)
        )

    def send_json_export_email(self, access_token: str, user_device_id: str) -> dict:
        url = f"/v1/user/device-data/{user_device_id}/export/json/email"
        return self._request(
            "POST", "DeviceData", url, headers=self._get_auth_headers(access_token)
        )
