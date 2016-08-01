package com.crontab.cvsInfo;

import java.sql.Connection;
import java.sql.PreparedStatement;

import com.crontab.util.ConnectionPool;

public class ConnectionTravel {
	public static void deleteTravel() throws Exception {
		Connection con = null;
		PreparedStatement pstmt = null;
		
		try {
			con = ConnectionPool.getConnection();

			String sql = "delete from sl_travel";
			
			pstmt = con.prepareStatement(sql);
			
			pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(pstmt != null) {
				pstmt.close();
			}
			if (con != null) {
				con.close();
			}
		}
	}
	
	public static void insertDaumTravel() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//daumTravel.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void insertNaverTravel() {
		String directory = "python C://Users//Hong//PycharmProjects//untitled//naverTravel.py";
		Runtime rt = Runtime.getRuntime();
		
		Process p;
		try {
			p = rt.exec(directory);
			p.getErrorStream().close();
			p.getInputStream().close();
			p.getOutputStream().close();
			p.waitFor();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}
